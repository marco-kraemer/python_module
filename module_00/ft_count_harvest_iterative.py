# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:47:02 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 17:03:48 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	x = range(1, int(input("Days until harvest: ")) + 1)
	for i in x:
		print("Day", i)
	print("Harvest time!")