import 'package:flutter/material.dart';
import 'package:smart_wallet_app/core/api.dart';
import 'package:smart_wallet_app/widgets/action_button.dart';
import 'package:smart_wallet_app/widgets/balance_card.dart';
import 'package:smart_wallet_app/widgets/transactions.dart';
import 'cashin_screen.dart';
import 'cashout_screen.dart';
import 'donate_screen.dart';
import 'invest_screen.dart';
import 'transfer_screen.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});
  static const id = "dashboard_screen";

  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final ApiService _apiService = ApiService();
  double? _balance;
  List<Map<String, dynamic>> _transactions = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _fetchDashboardData(); // Fetch balance and transactions on screen load
  }

  // Method to fetch balance and transactions
  Future<void> _fetchDashboardData() async {
    setState(() {
      _isLoading = true;
    });

    final balance = await _apiService.checkBalance();
    final transactions = await _apiService.fetchTransactions();

    setState(() {
      _balance = balance;
      _transactions = transactions ?? [];
      _isLoading = false;
    });
  }

  // Method to handle successful cash-in
  void _onTransactionSuccess() {
    _fetchDashboardData(); // Re-fetch the balance and transactions
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('eT3 Cash Dashboard'),
      ),
      body: _isLoading
          ? Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Display balance
                  BalanceCard(balance: _balance ?? 0.0),
                  SizedBox(height: 20),

                  // Quick action buttons
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ActionButton(
                        icon: Icons.arrow_downward,
                        label: 'Cash In',
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => CashInScreen(
                                onSuccess: _onTransactionSuccess,
                              ),
                            ),
                          );
                        },
                      ),
                      ActionButton(
                        icon: Icons.arrow_upward,
                        label: 'Cash Out',
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => CashOutScreen(
                                      onSuccess: _onTransactionSuccess,
                                    )),
                          );
                        },
                      ),
                      ActionButton(
                        icon: Icons.compare_arrows,
                        label: 'Transfer',
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => TransferScreen(
                                      onSuccess: _onTransactionSuccess,
                                    )),
                          );
                        },
                      ),
                    ],
                  ),
                  SizedBox(height: 20),

                  // Another row of quick actions
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ActionButton(
                        icon: Icons.volunteer_activism,
                        label: 'Donate',
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => DonateScreen(
                                      onSuccess: _onTransactionSuccess,
                                    )),
                          );
                        },
                      ),
                      ActionButton(
                        icon: Icons.trending_up,
                        label: 'Invest',
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => InvestScreen(
                                      onSuccess: _onTransactionSuccess,
                                    )),
                          );
                        },
                      ),
                    ],
                  ),
                  SizedBox(height: 20),

                  // Transaction history section
                  Text(
                    'Transaction History',
                    style: TextStyle(
                      fontSize: 18.0,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(height: 10),
                  TransactionList(transactions: _transactions),
                ],
              ),
            ),
    );
  }
}
