{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "You have 3 chances Remaining\n",
      "Guess a Number between 1 to 30 :22\n",
      "Your guess number is greater than win number\n",
      "\n",
      "You have 2 chances Remaining\n",
      "Guess a Number between 1 to 30 :2\n",
      "Your guess number is smaller than win number\n",
      "\n",
      "You have 1 chances Remaining\n",
      "Guess a Number between 1 to 30 :4\n",
      "Your guess number is smaller than win number\n",
      "\n",
      "Sorry You Lose, Please Try Again\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "win_number = random.randint(1,30)\n",
    "counter = 0\n",
    "chances = 3\n",
    "\n",
    "for i in range(3):\n",
    "    print(f\"\\nYou have {chances} chances Remaining\")\n",
    "    num = int(input(\"Guess a Number between 1 to 30 :\"))\n",
    "    chances -= 1\n",
    "    \n",
    "    if num == win_number:\n",
    "        counter += 1\n",
    "        print(\"\\nCongratulations, You Guess Correct Number in attempt no: \",counter)\n",
    "        break\n",
    "    \n",
    "    else:\n",
    "        \n",
    "        if num < win_number:\n",
    "            print(\"Your guess number is smaller than win number\")\n",
    "        \n",
    "        else:\n",
    "            print(\"Your guess number is greater than win number\")\n",
    "        \n",
    "        counter += 1\n",
    "        if counter == 3:\n",
    "            print(\"\\nSorry You Lose, Please Try Again\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
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
