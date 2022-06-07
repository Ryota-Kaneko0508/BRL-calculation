import streamlit as st

st.title('BRL式計算ツール')

st.sidebar.write("""
# BRL式計算ツール
こちらはBRL式計算ツールです。以下のオプションから変数の値を指定できます。
""")

# 質量
math = st.sidebar.number_input("・質量m[g]")
math *= pow(10, -3)

# 速度
velocity = st.sidebar.number_input("・飛翔体の速度v[m/s]")

# 外径
diameter = st.sidebar.number_input("・飛翔体の外径d[mm]")
diameter *= pow(10, -3)

# 板厚
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
