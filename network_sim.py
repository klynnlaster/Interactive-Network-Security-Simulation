import networkx as nx
import matplotlib.pyplot as plt
import random
import streamlit as st



# Create a network graph
G = nx.DiGraph()
G.add_edges_from([
    ("Client", "Router"),
    ("Router", "Server"),
    ("Router", "Firewall"),
    ("Firewall", "Server")
])

# Visualize the network
nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue")
plt.title("Network Topology")
plt.show()

def send_packet(src, dest, firewall_rules):
    if src == "Firewall" and dest in firewall_rules:
        return f"Packet blocked by firewall rule: {dest}"
    return f"Packet sent from {src} to {dest}"

firewall_rules = {"Server"}  # Block packets to the Server
print(send_packet("Router", "Firewall", firewall_rules))  # Simulate packet
print(send_packet("Firewall", "Server", firewall_rules))

packets = 100
blocked = 0
for _ in range(packets):
    result = send_packet("Firewall", "Server", firewall_rules)
    if "blocked" in result:
        blocked += 1

print(f"Packets sent: {packets}, Blocked: {blocked}, Success: {packets - blocked}")

st.title("Network Security Simulation")
packets = st.slider("Number of Packets", 10, 1000, 100)
block_server = st.checkbox("Block packets to Server")
firewall_rules = {"Server"} if block_server else {}

# Run Simulation
blocked = 0
for _ in range(packets):
    result = send_packet("Firewall", "Server", firewall_rules)
    if "blocked" in result:
        blocked += 1

st.write(f"Packets sent: {packets}")
st.write(f"Blocked: {blocked}")
st.write(f"Success: {packets - blocked}")

success = packets - blocked
labels = ["Blocked", "Success"]
sizes = [blocked, success]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)