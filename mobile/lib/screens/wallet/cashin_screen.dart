import 'package:flutter/material.dart';
import 'package:smart_wallet_app/core/api.dart';
import 'package:smart_wallet_app/widgets/action_card.dart';

class CashInScreen extends StatefulWidget {
  final Function onSuccess; // Callback to update balance and transactions

  const CashInScreen({Key? key, required this.onSuccess}) : super(key: key);

  @override
  _CashInScreenState createState() => _CashInScreenState();
}

class _CashInScreenState extends State<CashInScreen> {
  final TextEditingController _amountController = TextEditingController();

  void _onConfirm() async {
    final amountText = _amountController.text;

    if (amountText.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter an amount.')),
      );
      return;
    }

    // Convert amount to double
    final amount = double.tryParse(amountText);
    if (amount == null || amount <= 0) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a valid amount.')),
      );
      return;
    }

    // Implement the logic for cash in
    final response = await ApiService().cashIn(amount);

    if (response.containsKey('error')) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(response['error'])),
      );
    } else {
      // Notify the parent widget (DashboardScreen) to update the balance and transactions
      widget.onSuccess();
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Cash in successful!')),
      );
      Navigator.pop(context); // Go back to the previous screen
    }
  }

  void _onCancel() {
    Navigator.pop(context); // Go back to the previous screen
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Cash In'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ActionCard(
          title: 'Cash In',
          description: 'Enter the amount you want to deposit into your wallet.',
          content: TextField(
            controller: _amountController,
            keyboardType: TextInputType.number,
            decoration: InputDecoration(
              labelText: 'Amount',
              border: OutlineInputBorder(),
            ),
          ),
          onConfirm: _onConfirm,
          onCancel: _onCancel,
        ),
      ),
    );
  }
}
