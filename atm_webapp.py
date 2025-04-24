# atm_webapp.py
import streamlit as st

class ATM:
    def __init__(self):
        self.balance = 100000
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited ${amount}")
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.history.append(f"Withdrawn ${amount}")
        return f"Withdrawn ${amount}. New balance: ${self.balance}"

    def transfer(self, amount, recipient):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        self.history.append(f"Transferred ${amount} to {recipient}")
        return f"Transferred ${amount} to {recipient}. New balance: ${self.balance}"

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history


# Streamlit App
st.title("💳 Modern ATM Machine")

if 'atm' not in st.session_state:
    st.session_state.atm = ATM()

menu = st.sidebar.selectbox("Select Option", ["Deposit", "Withdraw", "Transfer", "Balance", "History"])

if menu == "Deposit":
    amount = st.number_input("Enter amount to deposit", min_value=1)
    if st.button("Deposit"):
        st.success(st.session_state.atm.deposit(amount))

elif menu == "Withdraw":
    amount = st.number_input("Enter amount to withdraw", min_value=1)
    if st.button("Withdraw"):
        st.success(st.session_state.atm.withdraw(amount))

elif menu == "Transfer":
    recipient = st.text_input("Recipient Name")
    amount = st.number_input("Amount to transfer", min_value=1)
    if st.button("Transfer"):
        st.success(st.session_state.atm.transfer(amount, recipient))

elif menu == "Balance":
    st.info(f"Current Balance: ${st.session_state.atm.get_balance()}")

elif menu == "History":
    history = st.session_state.atm.get_history()
    if history:
        for item in history:
            st.write(f"- {item}")
    else:
        st.write("No transactions yet.")
