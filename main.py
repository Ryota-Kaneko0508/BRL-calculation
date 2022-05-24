import streamlit as st

st.title('BRL式計算ツール')

st.sidebar.write("""
# BRL式計算ツール
こちらはBRL式計算ツールです。以下のオプションから変数の値を指定できます。
""")

math = st.sidebar.number_input("・質量m[g]")
math *= pow(10, -3)

velocity = st.sidebar.number_input("・飛翔体の速度v[m/s]")

diameter = st.sidebar.number_input("・飛翔体の外径d[mm]")
diameter *= pow(10, -3)

thickness = st.sidebar.number_input("・板の実測厚t[mm]")
thickness *= pow(10, -3)

st.write('')

if diameter == 0:
  st.write("""## BRL式による予測値t_brl: 外径の値を入力してください""")
else:
  t_brl = pow((0.5 * math * pow(velocity, 2)) / (1.4396 * pow(10, 9) * pow(diameter, 3/2)), 2/3) * 1000
  
  st.write(f"""## BRL式による予測値: {t_brl:.2f}[mm]""")
  
if thickness == 0:
  st.write(""" ## t_brl/t: 板の実測厚を入力してください ## """)
else:
  st.write(f"""## t_brl/t: {t_brl * pow(10, -3) /thickness:.2f}[-]""")
# st.write(f"""
# ### 過去 **{days}日間** のGAFA株価
# """)

# @st.cache
# def get_data(days, tickers):
#     df = pd.DataFrame()
#     for company in tickers.keys():
#         tkr = yf.Ticker(tickers[company])
#         hist = tkr.history(period=f'{days}d')
#         hist.index = hist.index.strftime('%d %B %Y')
#         hist = hist[['Close']]
#         hist.columns = [company]
#         hist = hist.T
#         hist.index.name = 'Name'
#         df = pd.concat([df, hist])
#     return df

# try: 
#     st.sidebar.write("""
#     ## 株価の範囲指定
#     """)
#     ymin, ymax = st.sidebar.slider(
#         '範囲を指定してください。',
#         0.0, 3500.0, (0.0, 3500.0)
#     )

#     tickers = {
#         'apple': 'AAPL',
#         'facebook': 'FB',
#         'google': 'GOOGL',
#         'microsoft': 'MSFT',
#         'netflix': 'NFLX',
#         'amazon': 'AMZN'
#     }
#     df = get_data(days, tickers)
#     companies = st.multiselect(
#         '会社名を選択してください。',
#         list(df.index),
#         ['google', 'amazon', 'facebook', 'apple']
#     )

#     if not companies:
#         st.error('少なくとも一社は選んでください。')
#     else:
#         data = df.loc[companies]
#         st.write("### 株価 (USD)", data.sort_index())
#         data = data.T.reset_index()
#         data = pd.melt(data, id_vars=['Date']).rename(
#             columns={'value': 'Stock Prices(USD)'}
#         )
#         chart = (
#             alt.Chart(data)
#             .mark_line(opacity=0.8, clip=True)
#             .encode(
#                 x="Date:T",
#                 y=alt.Y("Stock Prices(USD):Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
#                 color='Name:N'
#             )
#         )
#         st.altair_chart(chart, use_container_width=True)
# except:
#     st.error(
#         "おっと！なにかエラーが起きているようです。"
#     )