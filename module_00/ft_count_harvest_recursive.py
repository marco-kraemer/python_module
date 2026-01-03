# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:52:30 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 16:59:04 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	recurse(x, i):
	if (i <= x):
		print("Day", i)
		i += 1
		recurse(x, i)
	else:
		print("Harvest time!")

def	ft_count_harvest_recursive():
	x = int(input("Days until harvest: "))
	recurse(x, 1)