# retrieval_utils.py
import numpy as np
import pandas as pd

EARTH_KM = 6371.0

def haversine_km(lat1, lon1, lat2, lon2):
    a = np.radians([lat1, lon1, lat2, lon2])
    lat1, lon1, lat2, lon2 = a
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return float(2 * EARTH_KM * np.arcsin(np.sqrt(h)))

def haversine_vec(lat1, lon1, lat2_arr, lon2_arr):
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2_arr)
    lon2 = np.radians(lon2_arr)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * EARTH_KM * np.arcsin(np.sqrt(h))

def clip_radius(x, low=3.0, high=20.0):
    return max(low, min(high, x))

def get_user_radius(row):
    label = row["mobility_label"]
    tr = row["travel_range_km"]

    if pd.isna(tr):
        tr = 5.0

    base = clip_radius(2.0 * tr, low=3.0, high=20.0)

    if label == "one_area":
        return base
    elif label == "two_area":
        return clip_radius(base * 1.2, low=3.0, high=25.0)
    elif label == "explorer":
        return clip_radius(base * 1.5, low=5.0, high=30.0)
    else:
        return 10.0

def get_user_hubs(uid, mobility_row, hubs_df):
    label = mobility_row["mobility_label"]
    uh = hubs_df[hubs_df["user_id"] == uid].sort_values("hub_rank").copy()

    if label == "one_area":
        return uh.head(1)
    elif label == "two_area":
        return uh.head(2)
    elif label == "explorer":
        return uh.head(3)
    else:
        return pd.DataFrame(columns=uh.columns)

def retrieve_candidates_for_user(uid, businesses, mobility_df, hubs_df, user_visited, top_n=100):
    row = mobility_df[mobility_df["user_id"] == uid]
    if len(row) == 0:
        return pd.DataFrame()

    row = row.iloc[0]
    label = row["mobility_label"]
    radius_km = get_user_radius(row)

    visited = user_visited.get(uid, set())
    cand = businesses[~businesses["business_id"].isin(visited)].copy()

    selected_hubs = get_user_hubs(uid, row, hubs_df)

    if label == "sparse" or len(selected_hubs) == 0:
        out = cand.sort_values("visit_count", ascending=False).head(top_n).copy()
        out["retrieval_mode"] = "global_fallback"
        out["distance_km"] = np.nan
        out["radius_km"] = radius_km
        return out

    hub_dist_cols = []
    for i, (_, h) in enumerate(selected_hubs.iterrows(), start=1):
        dcol = f"dist_hub_{i}"
        cand[dcol] = haversine_vec(
            h["hub_lat"], h["hub_lon"],
            cand["latitude"].to_numpy(),
            cand["longitude"].to_numpy()
        )
        hub_dist_cols.append(dcol)

    cand["distance_km"] = cand[hub_dist_cols].min(axis=1)

    gated = cand[cand["distance_km"] <= radius_km].copy()

    if len(gated) < top_n:
        gated = cand[cand["distance_km"] <= radius_km * 1.5].copy()

    gated["pop_score"] = np.log1p(gated["visit_count"])
    gated["score"] = gated["pop_score"] - 0.1 * gated["distance_km"]

    gated = gated.sort_values(["score", "visit_count"], ascending=[False, False]).head(top_n).copy()
    gated["retrieval_mode"] = "hub_aware"
    gated["radius_km"] = radius_km
    return gated