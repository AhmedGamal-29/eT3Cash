import 'package:flutter/material.dart';
import 'package:smart_wallet_app/widgets/action_card.dart';
import 'package:smart_wallet_app/core/api.dart';

class InvestScreen extends StatefulWidget {
  final Function() onSuccess;

  InvestScreen({required this.onSuccess});

  @override
  _InvestScreenState createState() => _InvestScreenState();
}

class _InvestScreenState extends State<InvestScreen> {
  final TextEditingController _amountController = TextEditingController();
  final ApiService _apiService = ApiService();

  Map<String, dynamic>? _marketData; // Market data to hold stocks info
  String? _selectedStock; // Selected stock symbol
  bool _loadingMarketData = true;

  @override
  void initState() {
    super.initState();
    _fetchMarketData();
  }

  Future<void> _fetchMarketData() async {
    final data = await _apiService.getMarketData();
    setState(() {
      _marketData = data;
      _loadingMarketData = false;
      _selectedStock = _marketData?.keys.first; // Default to the first stock
    });
  }

  void _onConfirm() async {
    double? amount = double.tryParse(_amountController.text);
    if (amount == null || amount <= 0 || _selectedStock == null) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
            content: Text('Please select a stock and enter a valid amount')),
      );
      return;
    }

    final result =
        await _apiService.invest(amount, stockSymbol: _selectedStock!);

    if (result.containsKey('error')) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(result['error'])),
      );
    } else {
      widget.onSuccess();

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
            content:
                Text('Investment in $_selectedStock successful: \$${amount}')),
      );

      Navigator.pop(context);
    }
  }

  void _onCancel() {
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Invest'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: _loadingMarketData
            ? Center(child: CircularProgressIndicator()) // Show loading spinner
            : ActionCard(
                title: 'Invest',
                description:
                    'Select a stock and enter the amount you want to invest.',
                content: Column(
                  children: [
                    DropdownButtonFormField<String>(
                      value: _selectedStock,
                      items: _marketData!.keys.map((stock) {
                        final stockInfo = _marketData![stock];
                        return DropdownMenuItem<String>(
                          value: stock,
                          child: Text(
                              '${stockInfo['name']} (\$${stockInfo['price']})'),
                        );
                      }).toList(),
                      onChanged: (value) {
                        setState(() {
                          _selectedStock = value;
                        });
                      },
                      decoration: InputDecoration(
                        labelText: 'Select Stock',
                        border: OutlineInputBorder(),
                      ),
                    ),
                    SizedBox(height: 16.0),
                    TextField(
                      controller: _amountController,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        labelText: 'Amount',
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
