import math
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
'''print("Initializing Quantum AI circuit")
circuit= QuantumCircuit(1,1)
circuit.h(0)
circuit.measure(0,0)
simulator=AerSimulator()
job=simulator.run(circuit,shots=1000)
result= job.result()
counts=result.get_counts()
quantum_output=list(counts.keys())[0]
print(f"Quantum output: {quantum_output}")
if quantum_output=="0":
    print("AI Decision Approved (Path A)")
else:
    print("Ai Detection Rejected (Path B)")
print(f"Quantum results:{counts}")'''


'''ai_confidence=0.35
angle=2*math.acos(math.sqrt(1-ai_confidence))
circuit=QuantumCircuit(1,1)
circuit.ry(angle,0)
circuit.measure(0,0)
simulator=AerSimulator()
job=simulator.run(circuit,shots=1000)
result=job.result()
counts=result.get_counts()
print(f"\n Quantum Data Distribution: {counts}")
print(circuit.draw(output="text"))'''

'''print("Building Quantum Decision Network...")
ai_data=0.80
angle=2* math.acos(math.sqrt(1-ai_data))
circuit=QuantumCircuit(2,2)
circuit.ry(angle,0)
circuit.cx(0,1)
circuit.measure([0,1],[0,1])
simulator=AerSimulator()
job=simulator.run(circuit, shots=1000)
result=job.result()
counts=result.get_counts()
print(f"\n Decision Output Counts: {counts}")
print("\n Architect Diagram")
print(circuit.draw(output="text"))'''

print("Initialising Quantum Neural Network Layer...")
input_data=0.35
input_angle=2*math.acos(math.sqrt(1-input_data))
ai_weight_angle=0.17
circuit=QuantumCircuit(1,1)
circuit.ry(input_angle,0)
circuit.ry(ai_weight_angle,0)
circuit.measure(0,0)
simulator=AerSimulator()
job=simulator.run(circuit,shots=1000)
result=job.result()
counts=result.get_counts()
print(f"\n QNN Output Vector: {counts}")
print("\n Neural Network Layer Blueprint:")
print(circuit.draw(output="text"))
