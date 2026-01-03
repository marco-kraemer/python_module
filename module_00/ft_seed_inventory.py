# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 17:15:12 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 17:25:48 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(seed_type.capitalize(), "seeds", quantity, "packets available")
	elif unit == "grams":
		print(seed_type.capitalize(), "seeds", quantity, "grams total")
	elif unit == "area":
		print(seed_type.capitalize(), "seeds", quantity, "square meters")
	else:
		print("Unknown unit type")