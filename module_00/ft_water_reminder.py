# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: msantos2 <msantos2@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/03 16:41:55 by msantos2          #+#    #+#              #
#    Updated: 2026/01/03 16:45:49 by msantos2         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	x = int(input("Days since last watering: "))
	if x > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")