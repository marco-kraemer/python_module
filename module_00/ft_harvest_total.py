# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:32:25 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 16:35:43 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	x = int(input("Day 1 harvest: "))
	y = int(input("Day 2 harvest: "))
	z = int(input("Day 3 harvest: "))
	print("Total harvest: ", x + y + z)