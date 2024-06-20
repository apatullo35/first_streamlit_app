{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .AppleSystemUIFontMonospaced-Medium;\f1\fnil\fcharset0 .AppleSystemUIFontMonospaced-RegularItalic;}
{\colortbl;\red255\green255\blue255;\red80\green163\blue255;\red29\green29\blue36;\red255\green255\blue255;
\red146\green151\blue169;\red151\green211\blue255;\red255\green255\blue72;\red252\green83\blue89;\red101\green236\blue255;
\red111\green240\blue144;}
{\*\expandedcolortbl;;\cssrgb\c37647\c70588\c100000;\cssrgb\c14902\c15294\c18824;\cssrgb\c100000\c100000\c100000;
\cssrgb\c63922\c65882\c72157;\cssrgb\c65098\c86275\c100000;\cssrgb\c100000\c100000\c34902;\cssrgb\c100000\c42353\c42353;\cssrgb\c45098\c93725\c100000;
\cssrgb\c49020\c93725\c63137;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl390\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  streamlit \cf2 \strokec2 as\cf4 \strokec4  st\
\cf2 \strokec2 import\cf4 \strokec4  pandas \cf2 \strokec2 as\cf4 \strokec4  pd\
\cf2 \strokec2 import\cf4 \strokec4  numpy \cf2 \strokec2 as\cf4 \strokec4  np\
\
st\cf5 \strokec5 .\cf4 \strokec4 title\cf5 \strokec5 (\cf6 \strokec6 'Uber pickups in NYC'\cf5 \strokec5 )\cf4 \strokec4 \
\
DATE_COLUMN \cf7 \strokec7 =\cf4 \strokec4  \cf6 \strokec6 'date/time'\cf4 \strokec4 \
DATA_URL \cf7 \strokec7 =\cf4 \strokec4  \cf5 \strokec5 (\cf6 \strokec6 'https://s3-us-west-2.amazonaws.com/'\cf4 \strokec4 \
            \cf6 \strokec6 'streamlit-demo-data/uber-raw-data-sep14.csv.gz'\cf5 \strokec5 )\cf4 \strokec4 \
\
\pard\pardeftab720\sl390\partightenfactor0
\cf8 \strokec8 @st\cf5 \strokec5 .\cf8 \strokec8 cache_data\cf4 \strokec4 \
\pard\pardeftab720\sl390\partightenfactor0
\cf2 \strokec2 def\cf4 \strokec4  load_data\cf5 \strokec5 (\cf4 \strokec4 nrows\cf5 \strokec5 ):\cf4 \strokec4 \
    data \cf7 \strokec7 =\cf4 \strokec4  pd\cf5 \strokec5 .\cf4 \strokec4 read_csv\cf5 \strokec5 (\cf4 \strokec4 DATA_URL\cf5 \strokec5 ,\cf4 \strokec4  nrows\cf7 \strokec7 =\cf4 \strokec4 nrows\cf5 \strokec5 )\cf4 \strokec4 \
    lowercase \cf7 \strokec7 =\cf4 \strokec4  \cf2 \strokec2 lambda\cf4 \strokec4  x\cf5 \strokec5 :\cf4 \strokec4  \cf9 \strokec9 str\cf5 \strokec5 (\cf4 \strokec4 x\cf5 \strokec5 ).\cf4 \strokec4 lower\cf5 \strokec5 ()\cf4 \strokec4 \
    data\cf5 \strokec5 .\cf4 \strokec4 rename\cf5 \strokec5 (\cf4 \strokec4 lowercase\cf5 \strokec5 ,\cf4 \strokec4  axis\cf7 \strokec7 =\cf6 \strokec6 'columns'\cf5 \strokec5 ,\cf4 \strokec4  inplace\cf7 \strokec7 =\cf10 \strokec10 True\cf5 \strokec5 )\cf4 \strokec4 \
    data\cf5 \strokec5 [\cf4 \strokec4 DATE_COLUMN\cf5 \strokec5 ]\cf4 \strokec4  \cf7 \strokec7 =\cf4 \strokec4  pd\cf5 \strokec5 .\cf4 \strokec4 to_datetime\cf5 \strokec5 (\cf4 \strokec4 data\cf5 \strokec5 [\cf4 \strokec4 DATE_COLUMN\cf5 \strokec5 ])\cf4 \strokec4 \
    \cf2 \strokec2 return\cf4 \strokec4  data\
\
data_load_state \cf7 \strokec7 =\cf4 \strokec4  st\cf5 \strokec5 .\cf4 \strokec4 text\cf5 \strokec5 (\cf6 \strokec6 'Loading data...'\cf5 \strokec5 )\cf4 \strokec4 \
data \cf7 \strokec7 =\cf4 \strokec4  load_data\cf5 \strokec5 (\cf10 \strokec10 10000\cf5 \strokec5 )\cf4 \strokec4 \
data_load_state\cf5 \strokec5 .\cf4 \strokec4 text\cf5 \strokec5 (\cf6 \strokec6 "Done! (using st.cache_data)"\cf5 \strokec5 )\cf4 \strokec4 \
\
\cf2 \strokec2 if\cf4 \strokec4  st\cf5 \strokec5 .\cf4 \strokec4 checkbox\cf5 \strokec5 (\cf6 \strokec6 'Show raw data'\cf5 \strokec5 ):\cf4 \strokec4 \
    st\cf5 \strokec5 .\cf4 \strokec4 subheader\cf5 \strokec5 (\cf6 \strokec6 'Raw data'\cf5 \strokec5 )\cf4 \strokec4 \
    st\cf5 \strokec5 .\cf4 \strokec4 write\cf5 \strokec5 (\cf4 \strokec4 data\cf5 \strokec5 )\cf4 \strokec4 \
\
st\cf5 \strokec5 .\cf4 \strokec4 subheader\cf5 \strokec5 (\cf6 \strokec6 'Number of pickups by hour'\cf5 \strokec5 )\cf4 \strokec4 \
hist_values \cf7 \strokec7 =\cf4 \strokec4  np\cf5 \strokec5 .\cf4 \strokec4 histogram\cf5 \strokec5 (\cf4 \strokec4 data\cf5 \strokec5 [\cf4 \strokec4 DATE_COLUMN\cf5 \strokec5 ].\cf4 \strokec4 dt\cf5 \strokec5 .\cf4 \strokec4 hour\cf5 \strokec5 ,\cf4 \strokec4  bins\cf7 \strokec7 =\cf10 \strokec10 24\cf5 \strokec5 ,\cf4 \strokec4  \cf9 \strokec9 range\cf7 \strokec7 =\cf5 \strokec5 (\cf10 \strokec10 0\cf5 \strokec5 ,\cf10 \strokec10 24\cf5 \strokec5 ))[\cf10 \strokec10 0\cf5 \strokec5 ]\cf4 \strokec4 \
st\cf5 \strokec5 .\cf4 \strokec4 bar_chart\cf5 \strokec5 (\cf4 \strokec4 hist_values\cf5 \strokec5 )\cf4 \strokec4 \
\
\pard\pardeftab720\sl390\partightenfactor0

\f1\i \cf5 \strokec5 # Some number in the range 0-23
\f0\i0 \cf4 \strokec4 \
hour_to_filter \cf7 \strokec7 =\cf4 \strokec4  st\cf5 \strokec5 .\cf4 \strokec4 slider\cf5 \strokec5 (\cf6 \strokec6 'hour'\cf5 \strokec5 ,\cf4 \strokec4  \cf10 \strokec10 0\cf5 \strokec5 ,\cf4 \strokec4  \cf10 \strokec10 23\cf5 \strokec5 ,\cf4 \strokec4  \cf10 \strokec10 17\cf5 \strokec5 )\cf4 \strokec4 \
filtered_data \cf7 \strokec7 =\cf4 \strokec4  data\cf5 \strokec5 [\cf4 \strokec4 data\cf5 \strokec5 [\cf4 \strokec4 DATE_COLUMN\cf5 \strokec5 ].\cf4 \strokec4 dt\cf5 \strokec5 .\cf4 \strokec4 hour \cf7 \strokec7 ==\cf4 \strokec4  hour_to_filter\cf5 \strokec5 ]\cf4 \strokec4 \
\
st\cf5 \strokec5 .\cf4 \strokec4 subheader\cf5 \strokec5 (\cf6 \strokec6 'Map of all pickups at %s:00'\cf4 \strokec4  \cf7 \strokec7 %\cf4 \strokec4  hour_to_filter\cf5 \strokec5 )\cf4 \strokec4 \
st\cf5 \strokec5 .\cf9 \strokec9 map\cf5 \strokec5 (\cf4 \strokec4 filtered_data\cf5 \strokec5 )\cf4 \strokec4 \
}
