import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# Configuração inicial da interface
st.title("Um Presente Matemático!")
st.write("Clique no botão para visualizar a evolução da curva:")
st.latex(r"y = \frac{3}{4} \cdot \sqrt[3]{t^2} + \sqrt{16 - t^2} \cdot \sin(a \cdot \pi \cdot t)")

# Função para calcular y
def calculate_y(t, a):
    valid_mask = t**2 <= 16  # Garantir que a raiz não seja negativa
    y = np.zeros_like(t)     # Inicializa y com zeros
    y[valid_mask] = (3/4) * np.cbrt(t[valid_mask]**2) + np.sqrt(16 - t[valid_mask]**2) * np.sin(a * np.pi * t[valid_mask])
    return y

# Geração dos valores de t
t = np.linspace(-4, 4, 500)

# Botão para iniciar a animação
if st.button("Iniciar Animação"):
    fig = go.Figure()
    graph = st.plotly_chart(fig, use_container_width=True)  # Placeholder para o gráfico

    # Iterar sobre os valores de a
    for a in np.linspace(0, 8, 100):  # Variação de a para criar animação
        y = calculate_y(t, a)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=y, mode="lines", line=dict(color='red', width=1), name=f"a = {round(a, 2)}"))
        fig.update_layout(
            title=f"Evolução da Curva para a = {round(a, 2)}",
            xaxis_title="t",
            yaxis_title="y",
            xaxis=dict(range=[-9, 9]),
            yaxis=dict(range=[-5, 5]),
        )

        graph.plotly_chart(fig, use_container_width=True)
        time.sleep(0.1)  # Pausa para criar o efeito de animação

st.write("")
st.write("")