import 'package:flutter/material.dart';
import 'package:smart_wallet_app/widgets/action_card.dart';
import 'package:smart_wallet_app/core/api.dart';

class DonateScreen extends StatefulWidget {
  final Function() onSuccess; // Callback to refresh data

  DonateScreen({required this.onSuccess}); // Constructor to accept the callback

  @override
  _DonateScreenState createState() => _DonateScreenState();
}

class _DonateScreenState extends State<DonateScreen> {
  final TextEditingController _amountController = TextEditingController();
  final ApiService _apiService = ApiService();

  void _onConfirm() async {
    double? amount = double.tryParse(_amountController.text);
    if (amount == null || amount <= 0) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please enter a valid amount')),
      );
      return;
    }

    final result = await _apiService.donate(amount);

    if (result.containsKey('error')) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(result['error'])),
      );
    } else {
      // Call the callback to refresh the data in DashboardScreen
      widget.onSuccess();

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Donation successful: \$${amount}')),
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
        title: Text('Donate'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ActionCard(
          title: 'Donate',
          description: 'Enter the amount you want to donate.',
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
