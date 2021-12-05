# a, b = map(int, input().split())
# c, d = map(int, input().split())

# count = 0

# if min(a, b):
    


select(
        [
            CouponTable,
            CouponPolicyTable.c.discount_type,
            CouponPolicyTable.c.minimum_krw,
            CouponPolicyTable.c.minimum_eur,
            CouponPolicyTable.c.minimum_usd,
            CouponPolicyTable.c.discount_krw,
            CouponPolicyTable.c.discount_eur,
            CouponPolicyTable.c.discount_usd,
            CouponPolicyTable.c.created_at,
        ]
    )
    .where(
        and_(
            CouponTable.c.issued_to == user_id,
            CouponTable.c.expire_at > now,
            CouponTable.c.used_with.is_(None),
            or_(*limited_to_condition),
        )
    )
    .select_from(CouponTable.join(CouponPolicyTable, CouponTable.c.policy_id == CouponPolicyTable.c.id))
    .order_by(desc(CouponTable.c.issued_at))


select(
    [
        CouponTable,
        CouponPolicyTable.c.discount_type,
        CouponPolicyTable.c.minimum_krw,
        CouponPolicyTable.c.minimum_eur,
        CouponPolicyTable.c.minimum_usd,
        CouponPolicyTable.c.discount_krw,
        CouponPolicyTable.c.discount_eur,
        CouponPolicyTable.c.discount_usd,
        CouponPolicyTable.c.created_at,
    ]
)
.where(
    and_(
        CouponTable.c.limitet_to.in_(None, project_id, artist_id)
    )
)