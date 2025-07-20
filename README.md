**Overview
**
This module implements a rolling backtest framework that uses Adaptive PCA (APCA) to uncover latent factors in financial return data. It then applies various portfolio weighting methods to construct long-short portfolios and evaluates their out-of-sample performance relative to a benchmark.

**Purpose
**
The goal is to test how different factor-based portfolio construction methods perform over time using a rolling window approach. The strategy is flexible: it supports both classic weighting techniques (like equal weight, risk parity, momentum) and more advanced methods based on machine learning models like gradient boosting.

⸻

**How It Works
**	1.	Input: A time series DataFrame of asset returns (data_returns) is passed to the strategy.
	2.	Rolling Window: For each window:
	•	APCA is used to extract underlying factors and loadings.
	•	Factor returns are aggregated, and a weight method is selected.
	•	Assets are ranked by their exposure to each factor, and quintile-based signals are generated.
	•	Portfolios are built by going long the top decile and short the bottom, weighted by the chosen method.
	•	Net returns are computed, accounting for transaction cost and slippage.
	3.	Output: Portfolio returns are stored and compared across methods.

⸻

**Supported Weighting Methods
**
Out of the full set of supported methods, the current setup includes:
	•	equal
	•	risk_parity
	•	momentum
	•	maximin
	•	stochastic
	•	gradient_boosting

Other advanced methods like tail_risk_parity, entropy, random_forest, and kelly are available but currently commented out—you can easily enable them if needed.

⸻

**Evaluation
**
The strategy includes built-in visualization tools to assess performance:
	•	Cumulative Returns: Compare strategy vs. index
	•	Drawdowns: See risk over time
	•	Monthly Heatmaps: Visualize return seasonality across years

The method evaluate_strategies(index_returns) runs all strategies and generates these plots in one go.
