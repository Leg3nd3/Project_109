import statistics
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv");
readingScore = df["reading score"].to_list();

readingScore_mean = statistics.mean(readingScore);
readingScore_median = statistics.median(readingScore);
readingScore_mode = statistics.mode(readingScore);
readingScore_stdev = statistics.stdev(readingScore)

print("Mean is ", readingScore_mean);
print("Median is ", readingScore_median);
print("Mode is ", readingScore_mode);
print("Standard Deviation is ", readingScore_stdev);

first_std_deviation_start, first_std_deviation_end = readingScore_mean-readingScore_stdev, readingScore_mean+readingScore_stdev
second_std_deviation_start, second_std_deviation_end = readingScore_mean-readingScore_stdev*2, readingScore_mean+readingScore_stdev*2
third_std_deviation_start, third_std_deviation_end = readingScore_mean-readingScore_stdev*3, readingScore_mean+readingScore_stdev*3

thin_1_std_deviation = [result for result in readingScore if result> first_std_deviation_start and result<first_std_deviation_end]
thin_2_std_deviation = [result for result in readingScore if result> second_std_deviation_start and result<second_std_deviation_end]
thin_3_std_deviation = [result for result in readingScore if result> third_std_deviation_start and result<third_std_deviation_end]

print("{} percentage of data lies in the first standard deviation", (thin_1_std_deviation)*100/len(readingScore))
print("{} percentage of data lies in the second standard deviation", (thin_2_std_deviation)*100/len(readingScore))
print("{} percentage of data lies in the third standard deviation", (thin_3_std_deviation)*100/len(readingScore))