MODEL (
  name sqlmesh_sample.seed_model,
  kind SEED (
    path '$root/seeds/random_data.csv'
  ),
  columns (
    id INTEGER,
    item_id INTEGER,
    event_date DATE
  ),
  grain (id, event_date)
);
