import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FAN - Time 5B",
)

header = st.beta_container()
graphs = st.beta_container()


@st.cache
def get_data(path):
    data = pd.read_csv(path, low_memory=False, sep=",")
    return data


with header:
    st.title('FAN - Time 5B')
    st.subheader('Hackathon Batalha de Dados')

with graphs:

    data1 = get_data('./data/mat.csv')
    data2 = get_data('./data/port.csv')
    data = data1 + data2

    column = st.selectbox("Informe um campo", data.columns)

    if column:
        pulocation_dist = pd.DataFrame(data[column])

        _filter = st.selectbox(
            f"Selecione um valor da coluna {column}", pulocation_dist)

        if _filter:
            filtered = data[(data[column] == _filter)]

            st.write(filtered)
            st.area_chart(filtered)

        pulocation_dist = pd.DataFrame(data[column].value_counts()).head(50)
        st.area_chart(pulocation_dist)
