import datetime
import RollingStrategy
import models.StockData as StockData
import model.APCA as APCA
import pandas as pd
import models.FinancialMetrics as FinancialMetrics

start_date = datetime.datetime(2017, 1, 1)
end_date = datetime.datetime(2024, 1, 1)

stock_data - StockData.StockData(start_date, end_date)
returns = stock_data.returns
index_returns = stock_data.index_returns

returns.tail(3)

correlation_matrix = StockData.CorrelationMatrix(returns)

pca_analysis = APCA.ComponentsAnalysis(stock_data.returns)
pca_analysis.plot_scree()
pca_analysis.plot_cumulative_explained_variance()

strategy = RollingStrategy.RollingAPCAStrategy(returns, window_size=36, max_iterations=1000, transaction_cost=0.001,slippage=0.001)
index_cum_returns, portfolio_cum_returns = strategy.evaluate_strategies(index_returns)

index_test_rets = pd.DataFrame(index_cum_returns)
index_test_rets.rename(columns={'Open': 'Benchmark'}, inplace=True)

index_test_rets.head(3)

index_stats = FinancialMetrics.FinancialMetrics.summary_stats(index_test_rets)

index_stats

portfolio_test_rets = pd.DataFrame(portfolio_cum_returns)
portfolio_test_rets.head(3)

portfolio_stats = FinancialMetrics.FinancialMetrics.summary_stats(portfolio_test_rets, market=index_test_rets)

portfolio_stats
                              
