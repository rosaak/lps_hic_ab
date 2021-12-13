from pathlib import Path
import pandas as pd 
import streamlit as st

st.set_page_config(page_title="A/B Compartment", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def get_data(dir_path):    
    pngs = {file.name.replace('_pca01.png', ''): str(file) for file in Path(dir_path).glob('*.png')}
    df = pd.DataFrame(pngs.items(), columns=['name', 'path'])
    df["group"] = df.name.apply(lambda x: x.split("_")[1])
    df["resolution"] = df.name.apply(lambda x: x.split("_")[2])
    df["chr"] = df.name.apply(lambda x: x.split("_")[3])
    return df



def main(df):
    
    #chr = st.sidebar.selectbox("Chromosome", sorted(df.chr.unique()))
    # group = st.sidebar.selectbox("Group", df.group.unique())
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("Veh-S2")
        st.markdown('---')
        # print(df[(df.group == 'Veh-S2') & (df.chr == chr)])
        st.image(df[(df.group == 'Veh-S2') & (df.chr == chr)].path.values[0])
    with col2:
        st.markdown("LPS2hrs-S4")
        st.markdown('---')
        st.image(df[(df.group == 'LPS2hrs-S4') & (df.chr == chr)].path.values[0])
    with col3:
        st.markdown("LPS24hrs-S6")
        st.markdown('---')
        st.image(df[(df.group == 'LPS24hrs-S6') & (df.chr == chr)].path.values[0])
    with col4:
        st.markdown("Macro-ko-K2b")
        st.markdown('---')
        st.image(df[(df.group == 'Macro-ko-K2b') & (df.chr == chr)].path.values[0])
    with col5:
        st.markdown("Macro-cre-K2b")
        st.markdown('---')
        st.image(df[(df.group == 'Macro-cre-K2b') & (df.chr == chr)].path.values[0])
    st.markdown('---')
    
    
if __name__ == "__main__":
    df = get_data('plots')
    df2 = get_data('plots01')
    df3 = get_data('plots02')
    # st.dataframe(df.group.value_counts())
    # st.dataframe(df3.group.value_counts())
    
    # sidebar
    chr = st.sidebar.select_slider('Select chr', options=["chr" + str(i) for i in range(1,20)])
    res = st.sidebar.selectbox('Pick one resolution', ['100k', '40k'], index=0)

    
    dfx = df[df.resolution == res]  
    dfx2 = df2[df2.resolution == res] 
    dfx3 = df3[df3.resolution == res]
    
    st.markdown("## A/B compartment analysis - visulaization of the PCA")
    main(dfx)

    main(dfx2)
    
    main(dfx3)
    
    st.markdown("### Note")
    st.markdown(f"""- panal 1 : straigt from hicPCA
- panal 2 : same -min max sidebar values for all the plots
- panal 3 : same -min max sidebar values for all the plots and flipBigwigSignal
- check the [hicPCA](https://hicexplorer.readthedocs.io/en/latest/content/tools/hicPCA.html) [hicPlotMatrix](https://hicexplorer.readthedocs.io/en/latest/content/tools/hicPlotMatrix.html) and [a/b compartment analysis](https://hicexplorer.readthedocs.io/en/latest/content/example_usage.html?highlight=A%2FB%20compartments#a-b-compartment-analysis) for more details""") 
    