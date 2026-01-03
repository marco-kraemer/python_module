# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:25:28 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 16:32:14 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plot_area():
	print("Enter length: ", end="")
	x = int(input())
	print("Enter width: ", end="")
	y = int(input())
	print("Plot area: ", x * y)