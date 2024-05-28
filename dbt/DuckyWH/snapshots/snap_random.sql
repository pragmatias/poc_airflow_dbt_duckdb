{% snapshot snap_random %}

{{ config(
    target_schema=generate_schema_name('silver'),
    unique_key='id',
    strategy='timestamp',
    updated_at='date',
    invalidate_hard_deletes=True,
    tags=["sel_snap"],
)}}


select * from {{ source('raw','snap_random') }}

{% endsnapshot %}

