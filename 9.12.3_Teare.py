{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7287cb6f-d78a-4151-8d8e-37550467d2f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cefa6fcf-0a4c-4a2c-830f-da05ebd04cb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic = pd.read_csv('https://vincentarelbundock.github.io/' + 'Rdatasets/csv/carData/TitanicSurvival.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8c203fdd-16bc-453f-b3ca-9a1c567da770",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.precision', 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fdc544b0-f099-42b1-a0ee-8f4f871f81e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>survived</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>passengerClass</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Allen, Miss. Elisabeth Walton</td>\n",
       "      <td>yes</td>\n",
       "      <td>female</td>\n",
       "      <td>29.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Allison, Master. Hudson Trevor</td>\n",
       "      <td>yes</td>\n",
       "      <td>male</td>\n",
       "      <td>0.92</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Allison, Miss. Helen Loraine</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>2.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Allison, Mr. Hudson Joshua Crei</td>\n",
       "      <td>no</td>\n",
       "      <td>male</td>\n",
       "      <td>30.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allison, Mrs. Hudson J C (Bessi</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>25.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                        Unnamed: 0 survived     sex    age passengerClass\n",
       "0    Allen, Miss. Elisabeth Walton      yes  female  29.00            1st\n",
       "1   Allison, Master. Hudson Trevor      yes    male   0.92            1st\n",
       "2     Allison, Miss. Helen Loraine       no  female   2.00            1st\n",
       "3  Allison, Mr. Hudson Joshua Crei       no    male  30.00            1st\n",
       "4  Allison, Mrs. Hudson J C (Bessi       no  female  25.00            1st"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "11a73322-4d2f-4209-bfc6-f640004a3967",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>survived</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>passengerClass</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1304</th>\n",
       "      <td>Zabour, Miss. Hileni</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>14.5</td>\n",
       "      <td>3rd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1305</th>\n",
       "      <td>Zabour, Miss. Thamine</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3rd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1306</th>\n",
       "      <td>Zakarian, Mr. Mapriededer</td>\n",
       "      <td>no</td>\n",
       "      <td>male</td>\n",
       "      <td>26.5</td>\n",
       "      <td>3rd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1307</th>\n",
       "      <td>Zakarian, Mr. Ortin</td>\n",
       "      <td>no</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>3rd</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1308</th>\n",
       "      <td>Zimmerman, Mr. Leo</td>\n",
       "      <td>no</td>\n",
       "      <td>male</td>\n",
       "      <td>29.0</td>\n",
       "      <td>3rd</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Unnamed: 0 survived     sex   age passengerClass\n",
       "1304       Zabour, Miss. Hileni       no  female  14.5            3rd\n",
       "1305      Zabour, Miss. Thamine       no  female   NaN            3rd\n",
       "1306  Zakarian, Mr. Mapriededer       no    male  26.5            3rd\n",
       "1307        Zakarian, Mr. Ortin       no    male  27.0            3rd\n",
       "1308         Zimmerman, Mr. Leo       no    male  29.0            3rd"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4b219554-b89f-4717-84d2-d003632b68a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "titanic.columns = ['name', 'survived', 'sex', 'age', 'class']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0ce27626-c73d-423b-aad8-a401c2b73f6a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>survived</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Allen, Miss. Elisabeth Walton</td>\n",
       "      <td>yes</td>\n",
       "      <td>female</td>\n",
       "      <td>29.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Allison, Master. Hudson Trevor</td>\n",
       "      <td>yes</td>\n",
       "      <td>male</td>\n",
       "      <td>0.92</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Allison, Miss. Helen Loraine</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>2.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Allison, Mr. Hudson Joshua Crei</td>\n",
       "      <td>no</td>\n",
       "      <td>male</td>\n",
       "      <td>30.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Allison, Mrs. Hudson J C (Bessi</td>\n",
       "      <td>no</td>\n",
       "      <td>female</td>\n",
       "      <td>25.00</td>\n",
       "      <td>1st</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              name survived     sex    age class\n",
       "0    Allen, Miss. Elisabeth Walton      yes  female  29.00   1st\n",
       "1   Allison, Master. Hudson Trevor      yes    male   0.92   1st\n",
       "2     Allison, Miss. Helen Loraine       no  female   2.00   1st\n",
       "3  Allison, Mr. Hudson Joshua Crei       no    male  30.00   1st\n",
       "4  Allison, Mrs. Hudson J C (Bessi       no  female  25.00   1st"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7427b59b-6a9e-49fa-9e30-9b30adc17825",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1046.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>29.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>21.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>28.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>39.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>80.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           age\n",
       "count  1046.00\n",
       "mean     29.88\n",
       "std      14.41\n",
       "min       0.17\n",
       "25%      21.00\n",
       "50%      28.00\n",
       "75%      39.00\n",
       "max      80.00"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "titanic.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e80aace8-2ca7-4e90-babf-8594602d2c47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count      1309\n",
       "unique        2\n",
       "top       False\n",
       "freq        809\n",
       "Name: survived, dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(titanic.survived == 'yes').describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ec4dca6b-1d4e-41f2-a450-9fe24ac979e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using matplotlib backend: <object object at 0x0000024B1956C650>\n"
     ]
    }
   ],
   "source": [
    "%matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8febb80c-a412-4f11-8c59-2fbd16e48797",
   "metadata": {},
   "outputs": [],
   "source": [
    "histogram = titanic.hist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f312783a-1bc3-42df-9522-3763b0b60a1d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
