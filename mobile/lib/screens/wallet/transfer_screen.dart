import 'package:flutter/material.dart';
import 'package:smart_wallet_app/widgets/action_card.dart';
import 'package:smart_wallet_app/core/api.dart';

class TransferScreen extends StatefulWidget {
  final Function() onSuccess; // Callback to refresh data

  TransferScreen(
      {required this.onSuccess}); // Constructor to accept the callback

  @override
  _TransferScreenState createState() => _TransferScreenState();
}

class _TransferScreenState extends State<TransferScreen> {
  final TextEditingController _amountController = TextEditingController();
  final TextEditingController _recipientController = TextEditingController();
  final ApiService _apiService = ApiService();

  void _onConfirm() async {
    double? amount = double.tryParse(_amountController.text);
    String recipient = _recipientController.text;

    if (amount == null || amount <= 0) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a valid amount')),
      );
      return;
    }

    if (recipient.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a recipient')),
      );
      return;
    }

    final result = await _apiService.transfer(amount, recipient);

    if (result.containsKey('error')) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(result['error'])),
      );
    } else {
      // Call the callback to refresh the data in DashboardScreen
      widget.onSuccess();

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
            content: Text('Transfer successful: \$${amount} to $recipient')),
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
        title: Text('Transfer Money'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ActionCard(
          title: 'Transfer Money',
          description: 'Enter the amount and the recipient\'s name.',
          content: Column(
            children: [
              TextField(
                controller: _amountController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  labelText: 'Amount',
                  border: OutlineInputBorder(),
                ),
              ),
              SizedBox(height: 16.0),
              TextField(
                controller: _recipientController,
                decoration: InputDecoration(
                  labelText: 'Recipient',
                  border: OutlineInputBorder(),
                ),
              ),
            ],
          ),
          onConfirm: _onConfirm,
          onCancel: _onCancel,
        ),
      ),
    );
  }
}
