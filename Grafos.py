import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

estados = ["Aguascalientes", "Baja California", "Chiapas", "Durango", "Estado de México", "Guanajuato", "Hidalgo"]
G.add_nodes_from(estados)

conexiones = [("Aguascalientes", "Guanajuato", {"costo": 150}),
              ("Aguascalientes", "Zacatecas", {"costo": 200}),
              ("Baja California", "Baja California Sur", {"costo": 300}),
              ("Baja California", "Sonora", {"costo": 250}),
              ("Chiapas", "Tabasco", {"costo": 180}),
              ("Chiapas", "Veracruz", {"costo": 220}),
              ("Durango", "Zacatecas", {"costo": 120}),
              ("Estado de México", "Hidalgo", {"costo": 100}),
              ("Guanajuato", "Michoacán", {"costo": 170}),
              ("Guanajuato", "Querétaro", {"costo": 90}),
              ("Hidalgo", "Puebla", {"costo": 150}),
              ("Hidalgo", "Tlaxcala", {"costo": 80}),
              ("Tlaxcala", "Puebla", {"costo": 60})]

G.add_edges_from(conexiones)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'costo')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo de estados y sus relaciones con costos")
plt.show()

def costo_total(recorrido):
    costo = 0
    for i in range(len(recorrido) - 1):
        costo += G[recorrido[i]][recorrido[i+1]]['costo']
    return costo

recorrido_sin_repetir = list(nx.algorithms.hamiltonian_path(G))
costo_sin_repetir = costo_total(recorrido_sin_repetir)

print("Recorrido sin repetir estados:", recorrido_sin_repetir)
print("Costo total:", costo_sin_repetir)

recorrido_con_repetir = list(nx.algorithms.eulerian_path(G))
costo_con_repetir = costo_total(recorrido_con_repetir)

print("\nRecorrido con repetir estados:", recorrido_con_repetir)
print("Costo total:", costo_con_repetir)
