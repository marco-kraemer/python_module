# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:37:13 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 16:41:08 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	x = int(input("Enter plant age in days: "))
	if x > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")