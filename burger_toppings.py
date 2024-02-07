# by Kami Bigdely
# Split temporary variable

patty = 70  # [gr]
pickle = 20  # [gr]
tomatoes = 25  # [gr]
lettuce = 15  # [gr]
buns = 95  # [gr]

ny_patties_weight = 2 * patty
ny_pickles_weight = 4 * pickle
ny_tomatoes_weight = 3 * tomatoes
ny_lettuce_weight = 2 * lettuce
ny_buns_weight = 2 * buns

ny_burger_weight = ny_patties_weight + ny_pickles_weight + ny_tomatoes_weight + ny_lettuce_weight + ny_buns_weight
print("NY Burger Weight", ny_burger_weight)

kimchi = 30  # [gr]
mayo = 5  # [gr]
golden_fried_onion = 20  # [gr]

seoul_kimchi_burger_weight = (
    ny_patties_weight + ny_pickles_weight + ny_tomatoes_weight +
    kimchi + mayo + golden_fried_onion + ny_buns_weight
)
print("Seoul Kimchi Burger Weight", seoul_kimchi_burger_weight)
