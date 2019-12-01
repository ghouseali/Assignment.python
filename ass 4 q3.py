{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Movie Theater\n",
      "\n",
      "Enter Your Age to get your Ticket: 21\n",
      "Your Ticket is Price is $15\n"
     ]
    }
   ],
   "source": [
    "print(\"Welcome to Movie Theater\")\n",
    "while True:\n",
    "    age = input(\"\\nEnter Your Age to get your Ticket: \")\n",
    "    if age == 'q':\n",
    "        print(\"Enjoy your Movie :)\")\n",
    "        break\n",
    "    elif int(age) < 3:\n",
    "        print(\"Your Ticket is Free\")\n",
    "    elif int(age) >= 3 and int(age) <= 12:\n",
    "        print(\"Your Ticket is Price is $10\")\n",
    "    elif int(age) > 12:\n",
    "        print(\"Your Ticket is Price is $15\")                \n",
    "    else:\n",
    "        print(\"Invalid Input\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
