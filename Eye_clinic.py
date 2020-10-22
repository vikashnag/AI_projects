{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Eye clinic.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "mount_file_id": "1C8Ikx_nRx9At4CjW46TPVE_yRkQbLfsz",
      "authorship_tag": "ABX9TyOP5XQ4YV8jcgh3bA3Y8NgZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vikashnag/AI_projects/blob/main/Eye_clinic.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IAz_RfMHl7IC"
      },
      "source": [
        "IMPORTING LIBRRARIES"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QGoh_hh9af_d"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "%matplotlib inline"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tiF5bkr3mAMc"
      },
      "source": [
        "LOADING THE DATA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "H207-CHibZcf"
      },
      "source": [
        "eye_clinic= pd.read_excel('/content/drive/My Drive/EyeClinic_Sample.xlsx', parse_dates= True)"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XXOUdN5wmEqs"
      },
      "source": [
        "CHECKING THE FIRST FIVE ROWS OF DATA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xxfKudA2bkJ1",
        "outputId": "2a772d11-1714-40ee-dcd7-9c39d8ade01b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        }
      },
      "source": [
        "eye_clinic.head(5)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>CampCode</th>\n",
              "      <th>OrderDate</th>\n",
              "      <th>Camp Place Code</th>\n",
              "      <th>RtSph</th>\n",
              "      <th>LtSph</th>\n",
              "      <th>billdate</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>AYY1504489</td>\n",
              "      <td>2015-04-06</td>\n",
              "      <td>1</td>\n",
              "      <td>0.75</td>\n",
              "      <td>1.25</td>\n",
              "      <td>2015-04-23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>AYY1504489</td>\n",
              "      <td>2015-04-06</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2015-04-23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>AYY1504489</td>\n",
              "      <td>2015-04-06</td>\n",
              "      <td>1</td>\n",
              "      <td>0.50</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2015-04-23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>AYY1504489</td>\n",
              "      <td>2015-04-06</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2015-04-23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>AYY1504489</td>\n",
              "      <td>2015-04-06</td>\n",
              "      <td>1</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>2015-04-23</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "     CampCode  OrderDate  Camp Place Code  RtSph  LtSph   billdate\n",
              "0  AYY1504489 2015-04-06                1   0.75   1.25 2015-04-23\n",
              "1  AYY1504489 2015-04-06                1   0.00   0.00 2015-04-23\n",
              "2  AYY1504489 2015-04-06                1   0.50   0.00 2015-04-23\n",
              "3  AYY1504489 2015-04-06                1   0.00   0.00 2015-04-23\n",
              "4  AYY1504489 2015-04-06                1  -1.00  -1.00 2015-04-23"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oPaae1LGmM_h"
      },
      "source": [
        "CHECKING THE THE DATA TYPES IN THE DATA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3ftlbj16bw8i",
        "outputId": "020f5720-3206-46e2-cfcf-a894263a66ff",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "source": [
        "eye_clinic.info()"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 20056 entries, 0 to 20055\n",
            "Data columns (total 6 columns):\n",
            " #   Column           Non-Null Count  Dtype         \n",
            "---  ------           --------------  -----         \n",
            " 0   CampCode         20056 non-null  object        \n",
            " 1   OrderDate        20056 non-null  datetime64[ns]\n",
            " 2   Camp Place Code  20056 non-null  int64         \n",
            " 3   RtSph            20056 non-null  float64       \n",
            " 4   LtSph            20056 non-null  float64       \n",
            " 5   billdate         19609 non-null  datetime64[ns]\n",
            "dtypes: datetime64[ns](2), float64(2), int64(1), object(1)\n",
            "memory usage: 940.2+ KB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5t17EpFkRIaP"
      },
      "source": [
        "CHECKING FOR MISSING VALUES IN THE DATA"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FaO2lZNFcNEU",
        "outputId": "393f6bff-bd5f-42d4-9803-33825397aa72",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 359
        }
      },
      "source": [
        "sns.heatmap(eye_clinic.isnull(), cmap= 'Blues', cbar= False, yticklabels= False)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fe32a10f6a0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 6
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4K71IWjumfw8"
      },
      "source": [
        "There are some missing values in the billdate column."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "30zWxcnXq8v3",
        "outputId": "5c68ea52-568d-4fd5-d5ab-14fb84b8cb45",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        }
      },
      "source": [
        "eye_clinic[eye_clinic['billdate'].isnull()]"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>CampCode</th>\n",
              "      <th>OrderDate</th>\n",
              "      <th>Camp Place Code</th>\n",
              "      <th>RtSph</th>\n",
              "      <th>LtSph</th>\n",
              "      <th>billdate</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>85</th>\n",
              "      <td>THI1504495</td>\n",
              "      <td>2015-04-14</td>\n",
              "      <td>7</td>\n",
              "      <td>0.50</td>\n",
              "      <td>0.5</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>122</th>\n",
              "      <td>SAM1504497</td>\n",
              "      <td>2015-04-14</td>\n",
              "      <td>6</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>123</th>\n",
              "      <td>SAM1504497</td>\n",
              "      <td>2015-04-15</td>\n",
              "      <td>6</td>\n",
              "      <td>1.00</td>\n",
              "      <td>1.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>242</th>\n",
              "      <td>SAM1504497</td>\n",
              "      <td>2015-04-14</td>\n",
              "      <td>6</td>\n",
              "      <td>1.00</td>\n",
              "      <td>1.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>296</th>\n",
              "      <td>ATH1504503</td>\n",
              "      <td>2015-04-20</td>\n",
              "      <td>10</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17082</th>\n",
              "      <td>MEL1612782</td>\n",
              "      <td>2016-12-13</td>\n",
              "      <td>332</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>-1.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17850</th>\n",
              "      <td>THI1701820</td>\n",
              "      <td>2017-01-06</td>\n",
              "      <td>352</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18032</th>\n",
              "      <td>ATH1701841</td>\n",
              "      <td>2017-01-23</td>\n",
              "      <td>35</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19400</th>\n",
              "      <td>EAM1703933</td>\n",
              "      <td>2017-03-13</td>\n",
              "      <td>382</td>\n",
              "      <td>0.75</td>\n",
              "      <td>0.5</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19787</th>\n",
              "      <td>ATH1703952</td>\n",
              "      <td>2017-03-28</td>\n",
              "      <td>35</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>NaT</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>447 rows × 6 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "         CampCode  OrderDate  Camp Place Code  RtSph  LtSph billdate\n",
              "85     THI1504495 2015-04-14                7   0.50    0.5      NaT\n",
              "122    SAM1504497 2015-04-14                6   0.00    0.0      NaT\n",
              "123    SAM1504497 2015-04-15                6   1.00    1.0      NaT\n",
              "242    SAM1504497 2015-04-14                6   1.00    1.0      NaT\n",
              "296    ATH1504503 2015-04-20               10   0.00    0.0      NaT\n",
              "...           ...        ...              ...    ...    ...      ...\n",
              "17082  MEL1612782 2016-12-13              332  -1.00   -1.0      NaT\n",
              "17850  THI1701820 2017-01-06              352   0.00    0.0      NaT\n",
              "18032  ATH1701841 2017-01-23               35   0.00    0.0      NaT\n",
              "19400  EAM1703933 2017-03-13              382   0.75    0.5      NaT\n",
              "19787  ATH1703952 2017-03-28               35   0.00    0.0      NaT\n",
              "\n",
              "[447 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TwKZfogOmo3m"
      },
      "source": [
        "DROPPING THE MISSING VALUES"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zQHIbOZ9IspR"
      },
      "source": [
        "eye_clinic= eye_clinic.dropna()"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WRnZHYSsLcht",
        "outputId": "bab5c64c-ca6d-400c-daad-9982c981ae49",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 359
        }
      },
      "source": [
        "sns.heatmap(eye_clinic.isnull(), cmap= 'Blues', cbar= False, yticklabels= False)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x7fe32a17d710>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HfxhjxtmnVsG"
      },
      "source": [
        "FINDING THE MOST SELLING LENSES IN RTSPH COLUMN."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-8xZSG12fx7t",
        "outputId": "5a32fe72-8cfe-49c7-a049-ffbcb3df9029",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "lenses= [-0.5, -0.75, -1.0, -1.25, -1.5, -1.75, -2.0, -2.25, -2.50, -3.0, -3.5, -4.0, -4.5, -5.0, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\n",
        "\n",
        "counter=0\n",
        "right_lens=[]\n",
        "for i in lenses:\n",
        "  for j in eye_clinic['RtSph']:\n",
        "    if j == i:\n",
        "      counter= counter + 1\n",
        "  print(\"Number of {} sph lens sold is {}:\".format(i, counter))\n",
        "  right_lens.append(counter)\n",
        "\n"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Number of -0.5 sph lens sold is 337:\n",
            "Number of -0.75 sph lens sold is 698:\n",
            "Number of -1.0 sph lens sold is 1095:\n",
            "Number of -1.25 sph lens sold is 1241:\n",
            "Number of -1.5 sph lens sold is 1587:\n",
            "Number of -1.75 sph lens sold is 1661:\n",
            "Number of -2.0 sph lens sold is 1898:\n",
            "Number of -2.25 sph lens sold is 1930:\n",
            "Number of -2.5 sph lens sold is 2067:\n",
            "Number of -3.0 sph lens sold is 2152:\n",
            "Number of -3.5 sph lens sold is 2200:\n",
            "Number of -4.0 sph lens sold is 2236:\n",
            "Number of -4.5 sph lens sold is 2248:\n",
            "Number of -5.0 sph lens sold is 2260:\n",
            "Number of 0.5 sph lens sold is 2993:\n",
            "Number of 0.75 sph lens sold is 3730:\n",
            "Number of 1.0 sph lens sold is 4718:\n",
            "Number of 1.25 sph lens sold is 5103:\n",
            "Number of 1.5 sph lens sold is 5748:\n",
            "Number of 2.0 sph lens sold is 6020:\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YlptaaSCtYHG",
        "outputId": "56ed5623-412a-48a5-c89a-6f1ec4b078ef",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "right_lens"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[337,\n",
              " 698,\n",
              " 1095,\n",
              " 1241,\n",
              " 1587,\n",
              " 1661,\n",
              " 1898,\n",
              " 1930,\n",
              " 2067,\n",
              " 2152,\n",
              " 2200,\n",
              " 2236,\n",
              " 2248,\n",
              " 2260,\n",
              " 2993,\n",
              " 3730,\n",
              " 4718,\n",
              " 5103,\n",
              " 5748,\n",
              " 6020]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w9h-3JRfNrmY",
        "outputId": "1bbf8ad0-0467-4876-804f-392ed54c3497",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "len(right_lens)"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f8bg4YmDoLMr"
      },
      "source": [
        "FINDING THE MOST SELLING LENSES IN LTSPH COLUMN."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yvqeEk8IwSUE",
        "outputId": "008999a2-4db0-4ad9-ec0e-25d168f1e1cc",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "lenses= [-0.5, -0.75, -1.0, -1.25, -1.5, -1.75, -2.0, -2.25, -2.50, -3.0, -3.5, -4.0, -4.5, -5.0, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0]\n",
        "\n",
        "counter= 0\n",
        "left_lens=[]\n",
        "for i in lenses:\n",
        "  for j in eye_clinic['LtSph']:\n",
        "    if j == i:\n",
        "      counter= counter + 1\n",
        "  print(\"Number of {} sph lens sold is {}:\".format(i, counter))\n",
        "  left_lens.append(counter)\n"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Number of -0.5 sph lens sold is 350:\n",
            "Number of -0.75 sph lens sold is 638:\n",
            "Number of -1.0 sph lens sold is 1037:\n",
            "Number of -1.25 sph lens sold is 1180:\n",
            "Number of -1.5 sph lens sold is 1505:\n",
            "Number of -1.75 sph lens sold is 1565:\n",
            "Number of -2.0 sph lens sold is 1759:\n",
            "Number of -2.25 sph lens sold is 1793:\n",
            "Number of -2.5 sph lens sold is 1930:\n",
            "Number of -3.0 sph lens sold is 2007:\n",
            "Number of -3.5 sph lens sold is 2049:\n",
            "Number of -4.0 sph lens sold is 2075:\n",
            "Number of -4.5 sph lens sold is 2094:\n",
            "Number of -5.0 sph lens sold is 2103:\n",
            "Number of 0.5 sph lens sold is 2864:\n",
            "Number of 0.75 sph lens sold is 3638:\n",
            "Number of 1.0 sph lens sold is 4559:\n",
            "Number of 1.25 sph lens sold is 4922:\n",
            "Number of 1.5 sph lens sold is 5503:\n",
            "Number of 2.0 sph lens sold is 5750:\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BIHtV1kgwZim",
        "outputId": "a0be84a9-1c1b-43c0-a166-26e2f73ab976",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "left_lens"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[350,\n",
              " 638,\n",
              " 1037,\n",
              " 1180,\n",
              " 1505,\n",
              " 1565,\n",
              " 1759,\n",
              " 1793,\n",
              " 1930,\n",
              " 2007,\n",
              " 2049,\n",
              " 2075,\n",
              " 2094,\n",
              " 2103,\n",
              " 2864,\n",
              " 3638,\n",
              " 4559,\n",
              " 4922,\n",
              " 5503,\n",
              " 5750]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MET4vqWbNvbU",
        "outputId": "0f737413-1de2-4376-cea0-93facb544f88",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "len(left_lens)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6yCypU-co3do"
      },
      "source": [
        "FINDING THE TOTAL NUMBER OF LENSES SOLD OF EACH TYPE "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hYQogx7LwcON",
        "outputId": "fbd7d72e-8e75-4a27-8a4a-847d99e4fd6e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "total_lens = [] \n",
        "\n",
        "for i in range(0, len(right_lens)): \n",
        "    total_lens.append(right_lens[i] + left_lens[i]) \n",
        "    print(\"Total number of {} sph lens sold is {}\".format(lenses[i], total_lens[i]))"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Total number of -0.5 sph lens sold is 687\n",
            "Total number of -0.75 sph lens sold is 1336\n",
            "Total number of -1.0 sph lens sold is 2132\n",
            "Total number of -1.25 sph lens sold is 2421\n",
            "Total number of -1.5 sph lens sold is 3092\n",
            "Total number of -1.75 sph lens sold is 3226\n",
            "Total number of -2.0 sph lens sold is 3657\n",
            "Total number of -2.25 sph lens sold is 3723\n",
            "Total number of -2.5 sph lens sold is 3997\n",
            "Total number of -3.0 sph lens sold is 4159\n",
            "Total number of -3.5 sph lens sold is 4249\n",
            "Total number of -4.0 sph lens sold is 4311\n",
            "Total number of -4.5 sph lens sold is 4342\n",
            "Total number of -5.0 sph lens sold is 4363\n",
            "Total number of 0.5 sph lens sold is 5857\n",
            "Total number of 0.75 sph lens sold is 7368\n",
            "Total number of 1.0 sph lens sold is 9277\n",
            "Total number of 1.25 sph lens sold is 10025\n",
            "Total number of 1.5 sph lens sold is 11251\n",
            "Total number of 2.0 sph lens sold is 11770\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "peo_n07u3r7e"
      },
      "source": [
        "We can clearly see that the total number of +2.0 sph lenses sold is the maximum and the total number of -0.5 sph lenses sold is the minimum.  "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gByXgDFIylZ-",
        "outputId": "6330474c-3ab7-4d80-cc51-6e3a76387e46",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "total_lens"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[687,\n",
              " 1336,\n",
              " 2132,\n",
              " 2421,\n",
              " 3092,\n",
              " 3226,\n",
              " 3657,\n",
              " 3723,\n",
              " 3997,\n",
              " 4159,\n",
              " 4249,\n",
              " 4311,\n",
              " 4342,\n",
              " 4363,\n",
              " 5857,\n",
              " 7368,\n",
              " 9277,\n",
              " 10025,\n",
              " 11251,\n",
              " 11770]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WZ82_hcWPKYt",
        "outputId": "6e8d6fa8-02ff-49d3-e5c6-3d2eb436e4d9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "len(total_lens)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WTXQRvMS0eIG",
        "outputId": "021fe614-4c40-45e6-b9f9-f3944fd42185",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        }
      },
      "source": [
        "total_lens.sort(reverse= True)\n",
        "total_lens"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[11770,\n",
              " 11251,\n",
              " 10025,\n",
              " 9277,\n",
              " 7368,\n",
              " 5857,\n",
              " 4363,\n",
              " 4342,\n",
              " 4311,\n",
              " 4249,\n",
              " 4159,\n",
              " 3997,\n",
              " 3723,\n",
              " 3657,\n",
              " 3226,\n",
              " 3092,\n",
              " 2421,\n",
              " 2132,\n",
              " 1336,\n",
              " 687]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-TMR92FnLoxM"
      },
      "source": [
        "Since we have the total number of lenses sold for each type of lens. We can now put them in buckets in order of their importance. So the most important lenses will go in bucket B1, the 2nd important ones will go to bucket B2 and so on.\n",
        "\n",
        "So the buckets will contain lenses in the following order:\n",
        "\n",
        "1) B1 - +2.0, +1.5, +1.25, +1.0, +0.75\n",
        "\n",
        "2) B2 - +0.5, -5.0, -4.5, -4.0, -3.5\n",
        "\n",
        "3) B3 - -3.0, -2.5, -2.25, -2.0, -1.75\n",
        "\n",
        "4) B4- -1.5, -1.25, -1.0, -0.75, -0.5"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WX5Ho7nwYbds"
      },
      "source": [
        ""
      ],
      "execution_count": 19,
      "outputs": []
    }
  ]
}