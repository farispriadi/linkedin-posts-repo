import pandas as pd
import plotly.graph_objects as go 

 
url_csv = "produksi-kelapa-pekalongankab-2020-top-5.csv"

def set_barcolor(is_max):
    if is_max:
        return 'skyblue'
    return '#909090'

# Membuat dataframe
df = pd.read_csv(url_csv)

is_max_prod = list(df['produksi'] == df['produksi'].max())
color_list = list(map(set_barcolor,is_max_prod))

# Membuat Bar Chart
fig = go.Figure()

fig.add_traces([
                go.Bar(
                    x=df['kecamatan'],
                    y=df['produksi'],
                    marker=dict(color=color_list),
                    text=df['produksi'],
                    textposition='outside',
                    textfont=dict(size=14,color='#909090'),
                    width=0.6,
                    
                )
            ])

layout= dict(
    title=dict(
                text = "Produksi Kelapa di Kab Pekalongan 2020 (ton)",
                pad=dict(l=43),
                font=dict(color='#909090',size=20)
            ),
    plot_bgcolor='rgba(255,255,255,0)',
    paper_bgcolor='rgba(255,255,255,0)',
    height=600,
    width=800,
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        range=[0,550],autorange=False),
    xaxis=dict(
        ticks='outside',
        linecolor='rgb(204,204,204)',
        linewidth=2,
        color='#909090'),
    )

annotations = [dict(x=0, y=550,
            text="Bojong menyumbang 33% dari total produksi kelapa di Kab. Pekalongan,",
            showarrow=False,
            xanchor='left',
            xshift=-100,
            font=dict(
                color='#909090',
                size=14
                ),
            ),
            dict(x=0, y=525,
            text="menjadikan Bojong sebagai kecamatan dengan produksi kelapa terbanyak di tahun 2020.",
            showarrow=False,
            xanchor='left',
            xshift=-100,
            font=dict(
                color='#909090',
                size=14
                ),
            ),
        ]

fig.update_layout(layout,annotations=annotations)
fig.show()

