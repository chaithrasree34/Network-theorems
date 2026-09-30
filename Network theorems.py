# Network-theorems
# Electrical Network Theorems Calculator

print("===== NETWORK THEOREMS =====")
print("1. Thevenin's Theorem")
print("2. Norton's Theorem")
print("3. Superposition Theorem")
print("4. Maximum Power Transfer Theorem")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    # Thevenin's Theorem
    V = float(input("Enter source voltage (V): "))
    R1 = float(input("Enter series resistance R1 (Ohm): "))
    R2 = float(input("Enter load resistance R2 (Ohm): "))

    Vth = V * R2 / (R1 + R2)
    Rth = (R1 * R2) / (R1 + R2)

    print("\n--- Thevenin's Theorem ---")
    print("Thevenin Voltage =", Vth, "V")
    print("Thevenin Resistance =", Rth, "Ohm")

elif choice == 2:
    # Norton's Theorem
    V = float(input("Enter source voltage (V): "))
    R1 = float(input("Enter resistance R1 (Ohm): "))
    R2 = float(input("Enter resistance R2 (Ohm): "))

    Rn = (R1 * R2) / (R1 + R2)
    In = V / R1

    print("\n--- Norton's Theorem ---")
    print("Norton Current =", In, "A")
    print("Norton Resistance =", Rn, "Ohm")

elif choice == 3:
    # Superposition Theorem
    V1 = float(input("Enter voltage source V1 (V): "))
    V2 = float(input("Enter voltage source V2 (V): "))
    R = float(input("Enter resistance (Ohm): "))

    I1 = V1 / R
    I2 = V2 / R
    Itotal = I1 + I2

    print("\n--- Superposition Theorem ---")
    print("Current due to V1 =", I1, "A")
    print("Current due to V2 =", I2, "A")
    print("Total Current =", Itotal, "A")

elif choice == 4:
    # Maximum Power Transfer Theorem
    Vth = float(input("Enter Thevenin voltage (V): "))
    Rth = float(input("Enter Thevenin resistance (Ohm): "))

    RL = Rth
    Pmax = (Vth ** 2) / (4 * Rth)

    print("\n--- Maximum Power Transfer ---")
    print("Required Load Resistance =", RL, "Ohm")
    print("Maximum Power =", Pmax, "W")

else:
    print("Invalid choice!")
