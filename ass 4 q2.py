{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "cities = {\n",
    "    \"Karachi\" : {\n",
    "        \"Country\" : \"Pakistan\",\n",
    "        \"Population\" : \"15,741,000\",\n",
    "        \"Fact\" : \"It is the Sixth largest city in the world by city population.\"\n",
    "    }, \n",
    "    \"Lahore\" : {\n",
    "        \"Country\" : \"Pakistan\",\n",
    "        \"Population\" : \"12,188,000\",\n",
    "        \"Fact\" : \"It is also known as the 'City of Gardens' because of its many parks and gardens.\"\n",
    "    },\n",
    "    \"Islamabad\" : {\n",
    "        \"Country\" : \"Pakistan\",\n",
    "        \"Population\" : \"1,095,064\",\n",
    "        \"Fact\" : \"Islamabad is noted for its high standards of living, safety, and abundant greenery.\"\n",
    "    }\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "KARACHI\n",
      "\tCountry: Pakistan\n",
      "\tPopulation: 15,741,000\n",
      "\tFact: It is the Sixth largest city in the world by city population.\n",
      "\n",
      "LAHORE\n",
      "\tCountry: Pakistan\n",
      "\tPopulation: 12,188,000\n",
      "\tFact: It is also known as the 'City of Gardens' because of its many parks and gardens.\n",
      "\n",
      "ISLAMABAD\n",
      "\tCountry: Pakistan\n",
      "\tPopulation: 1,095,064\n",
      "\tFact: Islamabad is noted for its high standards of living, safety, and abundant greenery.\n"
     ]
    }
   ],
   "source": [
    "for city, city_info in cities.items():\n",
    "    print(\"\\n\" + city.upper())\n",
    "    country = city_info['Country']\n",
    "    pop = city_info['Population']\n",
    "    fact = city_info['Fact']\n",
    "    print(\"\\tCountry: \" + country)\n",
    "    print(\"\\tPopulation: \" + pop)\n",
    "    print(\"\\tFact: \" + fact)"
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
