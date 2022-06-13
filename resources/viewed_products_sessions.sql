drop table if exists viewed_products_session;
create table viewed_products_session as (
    select viewed_before.product_id as viewed_products, viewed_before.profile_id, sessions.id as session_id from (
        select * from viewed_before
        join buids on viewed_before.profile_id = buids.profile_id
        join sessions on buids.buid = sessions.buid
        order by viewed_before.profile_id
    ) as X
);