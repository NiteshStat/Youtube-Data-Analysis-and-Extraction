{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ab751e7c",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <h1 align=center>Data 1202: Data Analytics Tools</h1>\n",
    "    <h1 align=center>Assignment-4</h1>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b72c32ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Python Libraries\n",
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "import pymysql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7dcd6a89",
   "metadata": {},
   "outputs": [
    {
     "ename": "UnicodeDecodeError",
     "evalue": "'utf-8' codec can't decode byte 0x80 in position 582: invalid start byte",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m                        Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Reading csv file \u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myoutube_dataset.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\util\\_decorators.py:211\u001b[0m, in \u001b[0;36mdeprecate_kwarg.<locals>._deprecate_kwarg.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    209\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    210\u001b[0m         kwargs[new_arg_name] \u001b[38;5;241m=\u001b[39m new_arg_value\n\u001b[1;32m--> 211\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\util\\_decorators.py:331\u001b[0m, in \u001b[0;36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    325\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) \u001b[38;5;241m>\u001b[39m num_allow_args:\n\u001b[0;32m    326\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[0;32m    327\u001b[0m         msg\u001b[38;5;241m.\u001b[39mformat(arguments\u001b[38;5;241m=\u001b[39m_format_argument_list(allow_args)),\n\u001b[0;32m    328\u001b[0m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[0;32m    329\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39mfind_stack_level(),\n\u001b[0;32m    330\u001b[0m     )\n\u001b[1;32m--> 331\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:950\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    935\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m    936\u001b[0m     dialect,\n\u001b[0;32m    937\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    946\u001b[0m     defaults\u001b[38;5;241m=\u001b[39m{\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdelimiter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m\"\u001b[39m},\n\u001b[0;32m    947\u001b[0m )\n\u001b[0;32m    948\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m--> 950\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:605\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    602\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    604\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 605\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    607\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    608\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1442\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1439\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1441\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1442\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_engine(f, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mengine)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1753\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1750\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(msg)\n\u001b[0;32m   1752\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m-> 1753\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m mapping[engine](f, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions)\n\u001b[0;32m   1754\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1755\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\c_parser_wrapper.py:79\u001b[0m, in \u001b[0;36mCParserWrapper.__init__\u001b[1;34m(self, src, **kwds)\u001b[0m\n\u001b[0;32m     76\u001b[0m     kwds\u001b[38;5;241m.\u001b[39mpop(key, \u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[0;32m     78\u001b[0m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdtype\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m ensure_dtype_objs(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdtype\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[1;32m---> 79\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_reader \u001b[38;5;241m=\u001b[39m parsers\u001b[38;5;241m.\u001b[39mTextReader(src, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m     81\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39munnamed_cols \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_reader\u001b[38;5;241m.\u001b[39munnamed_cols\n\u001b[0;32m     83\u001b[0m \u001b[38;5;66;03m# error: Cannot determine type of 'names'\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\_libs\\parsers.pyx:547\u001b[0m, in \u001b[0;36mpandas._libs.parsers.TextReader.__cinit__\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\_libs\\parsers.pyx:636\u001b[0m, in \u001b[0;36mpandas._libs.parsers.TextReader._get_header\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\_libs\\parsers.pyx:852\u001b[0m, in \u001b[0;36mpandas._libs.parsers.TextReader._tokenize_rows\u001b[1;34m()\u001b[0m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\_libs\\parsers.pyx:1965\u001b[0m, in \u001b[0;36mpandas._libs.parsers.raise_parser_error\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mUnicodeDecodeError\u001b[0m: 'utf-8' codec can't decode byte 0x80 in position 582: invalid start byte"
     ]
    }
   ],
   "source": [
    "#Reading csv file \n",
    "df = pd.read_csv(\"youtube_dataset.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a28fed32",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Reading csv file \n",
    "df = pd.read_csv(\"youtube_dataset.csv\", encoding='latin-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "abcf2f4e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 3944 entries, 0 to 3943\n",
      "Data columns (total 20 columns):\n",
      " #   Column                 Non-Null Count  Dtype \n",
      "---  ------                 --------------  ----- \n",
      " 0   web-scraper-order      3944 non-null   object\n",
      " 1   web-scraper-start-url  3944 non-null   object\n",
      " 2   userID                 3944 non-null   object\n",
      " 3   userID-href            3944 non-null   object\n",
      " 4   name                   3944 non-null   object\n",
      " 5   uploads                3944 non-null   int64 \n",
      " 6   subscribers            3944 non-null   int64 \n",
      " 7   videoviews             3944 non-null   int64 \n",
      " 8   country                3650 non-null   object\n",
      " 9   channeltype            3681 non-null   object\n",
      " 10  usercreated            3944 non-null   object\n",
      " 11  grade                  3944 non-null   object\n",
      " 12  YouTube_Link           59 non-null     object\n",
      " 13  YouTube_Link-href      3885 non-null   object\n",
      " 14  TwitterHandle          52 non-null     object\n",
      " 15  TwitterHandle-href     3334 non-null   object\n",
      " 16  InstagramHandle        42 non-null     object\n",
      " 17  InstagramHandle-href   3885 non-null   object\n",
      " 18  MonthlyEarnings        3944 non-null   object\n",
      " 19  YearlyEarnings         3944 non-null   object\n",
      "dtypes: int64(3), object(17)\n",
      "memory usage: 616.4+ KB\n"
     ]
    }
   ],
   "source": [
    "#Understanding the dataframe\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "533e14ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Rows: 3944, Total Columns: 20\n"
     ]
    }
   ],
   "source": [
    "#understanding the shape of the dataframe \n",
    "total_rows, total_columns = df.shape\n",
    "print(f'Total Rows: {total_rows}, Total Columns: {total_columns}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1e209fdf",
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
       "      <th>web-scraper-order</th>\n",
       "      <th>web-scraper-start-url</th>\n",
       "      <th>userID</th>\n",
       "      <th>userID-href</th>\n",
       "      <th>name</th>\n",
       "      <th>uploads</th>\n",
       "      <th>subscribers</th>\n",
       "      <th>videoviews</th>\n",
       "      <th>country</th>\n",
       "      <th>channeltype</th>\n",
       "      <th>usercreated</th>\n",
       "      <th>grade</th>\n",
       "      <th>YouTube_Link</th>\n",
       "      <th>YouTube_Link-href</th>\n",
       "      <th>TwitterHandle</th>\n",
       "      <th>TwitterHandle-href</th>\n",
       "      <th>InstagramHandle</th>\n",
       "      <th>InstagramHandle-href</th>\n",
       "      <th>MonthlyEarnings</th>\n",
       "      <th>YearlyEarnings</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1553043067-5148</td>\n",
       "      <td>https://socialblade.com/youtube/top/5000/mosts...</td>\n",
       "      <td>PewDiePie</td>\n",
       "      <td>https://socialblade.com/youtube/c/pewdiepie</td>\n",
       "      <td>PewDiePie</td>\n",
       "      <td>3779</td>\n",
       "      <td>90210848</td>\n",
       "      <td>20772365682</td>\n",
       "      <td>US</td>\n",
       "      <td>Entertainment</td>\n",
       "      <td>Apr 29th, 2010</td>\n",
       "      <td>A</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UC-lHJZR3Gqxm24_Vd...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://twitter.com/pewdiepie</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://instagram.com/pewdiepie</td>\n",
       "      <td>66.9K - 1.1M</td>\n",
       "      <td>802.3K - 12.8M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1553043063-5147</td>\n",
       "      <td>https://socialblade.com/youtube/top/5000/mosts...</td>\n",
       "      <td>T-Series</td>\n",
       "      <td>https://socialblade.com/youtube/c/tseriesmusic</td>\n",
       "      <td>T-Series</td>\n",
       "      <td>13218</td>\n",
       "      <td>90194329</td>\n",
       "      <td>65092058996</td>\n",
       "      <td>IN</td>\n",
       "      <td>Music</td>\n",
       "      <td>Mar 13th, 2006</td>\n",
       "      <td>A++</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UCq-Fj5jknLsUf-MWS...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://instagram.com/tseries.official</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://plus.google.com/115156822320080163368</td>\n",
       "      <td>635.6K - 10.2M</td>\n",
       "      <td>7.6M - 122M</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1553043059-5146</td>\n",
       "      <td>https://socialblade.com/youtube/top/5000/mosts...</td>\n",
       "      <td>Gaming</td>\n",
       "      <td>https://socialblade.com/youtube/channel/UCOpNc...</td>\n",
       "      <td>Gaming</td>\n",
       "      <td>0</td>\n",
       "      <td>81888222</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Games</td>\n",
       "      <td>Dec 15th, 2013</td>\n",
       "      <td>D-</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UCOpNcN46UbXVtpKMr...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UCOpNcN46UbXVtpKMr...</td>\n",
       "      <td>0 - 0</td>\n",
       "      <td>0 - 0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1553043055-5145</td>\n",
       "      <td>https://socialblade.com/youtube/top/5000/mosts...</td>\n",
       "      <td>YouTube Movies</td>\n",
       "      <td>https://socialblade.com/youtube/channel/UClgRk...</td>\n",
       "      <td>YouTube Movies</td>\n",
       "      <td>0</td>\n",
       "      <td>77413743</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Film</td>\n",
       "      <td>Jun 10th, 2015</td>\n",
       "      <td>D-</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UClgRkhTL3_hImCAmd...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UClgRkhTL3_hImCAmd...</td>\n",
       "      <td>0 - 0</td>\n",
       "      <td>0 - 0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1553043051-5144</td>\n",
       "      <td>https://socialblade.com/youtube/top/5000/mosts...</td>\n",
       "      <td>Sports</td>\n",
       "      <td>https://socialblade.com/youtube/channel/UCEgdi...</td>\n",
       "      <td>Sports</td>\n",
       "      <td>0</td>\n",
       "      <td>75622870</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Sports</td>\n",
       "      <td>Dec 15th, 2013</td>\n",
       "      <td>D-</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...</td>\n",
       "      <td>0 - 0</td>\n",
       "      <td>0 - 0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  web-scraper-order                              web-scraper-start-url  \\\n",
       "0   1553043067-5148  https://socialblade.com/youtube/top/5000/mosts...   \n",
       "1   1553043063-5147  https://socialblade.com/youtube/top/5000/mosts...   \n",
       "2   1553043059-5146  https://socialblade.com/youtube/top/5000/mosts...   \n",
       "3   1553043055-5145  https://socialblade.com/youtube/top/5000/mosts...   \n",
       "4   1553043051-5144  https://socialblade.com/youtube/top/5000/mosts...   \n",
       "\n",
       "           userID                                        userID-href  \\\n",
       "0       PewDiePie        https://socialblade.com/youtube/c/pewdiepie   \n",
       "1        T-Series     https://socialblade.com/youtube/c/tseriesmusic   \n",
       "2          Gaming  https://socialblade.com/youtube/channel/UCOpNc...   \n",
       "3  YouTube Movies  https://socialblade.com/youtube/channel/UClgRk...   \n",
       "4          Sports  https://socialblade.com/youtube/channel/UCEgdi...   \n",
       "\n",
       "             name  uploads  subscribers   videoviews country    channeltype  \\\n",
       "0       PewDiePie     3779     90210848  20772365682      US  Entertainment   \n",
       "1        T-Series    13218     90194329  65092058996      IN          Music   \n",
       "2          Gaming        0     81888222            0     NaN          Games   \n",
       "3  YouTube Movies        0     77413743            0     NaN           Film   \n",
       "4          Sports        0     75622870            0     NaN         Sports   \n",
       "\n",
       "      usercreated grade YouTube_Link  \\\n",
       "0  Apr 29th, 2010     A          NaN   \n",
       "1  Mar 13th, 2006   A++          NaN   \n",
       "2  Dec 15th, 2013    D-          NaN   \n",
       "3  Jun 10th, 2015    D-          NaN   \n",
       "4  Dec 15th, 2013    D-          NaN   \n",
       "\n",
       "                                   YouTube_Link-href TwitterHandle  \\\n",
       "0  https://youtube.com/channel/UC-lHJZR3Gqxm24_Vd...           NaN   \n",
       "1  https://youtube.com/channel/UCq-Fj5jknLsUf-MWS...           NaN   \n",
       "2  https://youtube.com/channel/UCOpNcN46UbXVtpKMr...           NaN   \n",
       "3  https://youtube.com/channel/UClgRkhTL3_hImCAmd...           NaN   \n",
       "4  https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...           NaN   \n",
       "\n",
       "                       TwitterHandle-href InstagramHandle  \\\n",
       "0           https://twitter.com/pewdiepie             NaN   \n",
       "1  https://instagram.com/tseries.official             NaN   \n",
       "2                                     NaN             NaN   \n",
       "3                                     NaN             NaN   \n",
       "4                                     NaN             NaN   \n",
       "\n",
       "                                InstagramHandle-href   MonthlyEarnings  \\\n",
       "0                    https://instagram.com/pewdiepie    66.9K - 1.1M   \n",
       "1      https://plus.google.com/115156822320080163368  635.6K - 10.2M   \n",
       "2  https://youtube.com/channel/UCOpNcN46UbXVtpKMr...           0 - 0   \n",
       "3  https://youtube.com/channel/UClgRkhTL3_hImCAmd...           0 - 0   \n",
       "4  https://youtube.com/channel/UCEgdi0XIXXZ-qJOFP...           0 - 0   \n",
       "\n",
       "     YearlyEarnings  \n",
       "0  802.3K - 12.8M  \n",
       "1     7.6M - 122M  \n",
       "2           0 - 0  \n",
       "3           0 - 0  \n",
       "4           0 - 0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#looking at the top five data \n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd7be7ee",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <h3 align=center>Create a function to calculate the distribution of channeltype from the top 1000 records.</h3>\n",
    "    \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d8e997a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#creating function name channeltype  \n",
    "def channeltype(data):\n",
    "    #getting first 1000 records uisng iloc\n",
    "    top_1000 = data.iloc[0:1000]\n",
    "    # Getting  the distribution of 'channeltype' values\n",
    "    distribution = top_1000['channeltype'].value_counts( )\n",
    "    # Getting the percentage of each 'channeltype' in the top 1000 records\n",
    "    percentage= distribution / len(top_1000) * 100\n",
    "    # Create a DataFrame with 'channeltype', 'Count', and 'Percentage' columns\n",
    "    result_table = pd.DataFrame({\n",
    "        'channeltype': distribution.index,\n",
    "        'Count': distribution.values,\n",
    "        'Percentage': percentage.values\n",
    "    })\n",
    "\n",
    "    # Return the DataFrame\n",
    "    return result_table "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c06313e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Calling the 'channeltype' function with the DataFrame 'df'\n",
    "dis = channeltype(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fade43b4",
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
       "      <th>channeltype</th>\n",
       "      <th>Count</th>\n",
       "      <th>Percentage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Entertainment</td>\n",
       "      <td>284</td>\n",
       "      <td>28.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Music</td>\n",
       "      <td>240</td>\n",
       "      <td>24.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Games</td>\n",
       "      <td>115</td>\n",
       "      <td>11.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Comedy</td>\n",
       "      <td>76</td>\n",
       "      <td>7.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>People</td>\n",
       "      <td>72</td>\n",
       "      <td>7.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Howto</td>\n",
       "      <td>49</td>\n",
       "      <td>4.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Film</td>\n",
       "      <td>36</td>\n",
       "      <td>3.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Education</td>\n",
       "      <td>30</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Tech</td>\n",
       "      <td>19</td>\n",
       "      <td>1.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Sports</td>\n",
       "      <td>17</td>\n",
       "      <td>1.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>News</td>\n",
       "      <td>17</td>\n",
       "      <td>1.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Autos</td>\n",
       "      <td>3</td>\n",
       "      <td>0.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Animals</td>\n",
       "      <td>2</td>\n",
       "      <td>0.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Nonprofit</td>\n",
       "      <td>1</td>\n",
       "      <td>0.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Travel</td>\n",
       "      <td>1</td>\n",
       "      <td>0.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      channeltype  Count  Percentage\n",
       "0   Entertainment    284        28.4\n",
       "1           Music    240        24.0\n",
       "2           Games    115        11.5\n",
       "3          Comedy     76         7.6\n",
       "4          People     72         7.2\n",
       "5           Howto     49         4.9\n",
       "6            Film     36         3.6\n",
       "7       Education     30         3.0\n",
       "8            Tech     19         1.9\n",
       "9          Sports     17         1.7\n",
       "10           News     17         1.7\n",
       "11          Autos      3         0.3\n",
       "12        Animals      2         0.2\n",
       "13      Nonprofit      1         0.1\n",
       "14         Travel      1         0.1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#viewing the  distribution of 'channeltype' values in the top 1000 rows of the DataFrame\n",
    "dis"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "64c4ff94",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <h3 align=center>Load only the top 1000 records of the original 4000 into a separate CSV file, and to a database table.</h3>\n",
    "    \n",
    "</div>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f08bd86c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#getting the top 1000 records \n",
    "top_1000 = df.iloc[0:1000]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6fe8150c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Save to CSV named top_1000_channels\n",
    "top_1000.to_csv(\"top_1000_channels.csv\", index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "179a0f67",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of the result: (1000, 20)\n"
     ]
    }
   ],
   "source": [
    "# Get the shape of the result\n",
    "result_shape = top_1000.shape\n",
    "print(f'Shape of the result: {result_shape}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f5e4605b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1000"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create the engine with the MySQL dialect and the appropriate connection details\n",
    "engine = create_engine('mysql+pymysql://group10:assignment4@localhost/assignment4')\n",
    "\n",
    "# Assuming 'your_dataframe' is the DataFrame you want to save\n",
    "top_1000.to_sql('top_1000_youtube_channels', con=engine, if_exists='replace', index=False)"
   ]
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
