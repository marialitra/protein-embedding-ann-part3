#!/usr/bin/env python3
"""
Create speed vs accuracy trade-off visualization
"""

import sys
import os

sys.path.append(os.path.dirname(__file__))

# Extract QPS from make search output
qps_data = {
    'LSH': 0.7010,
    'Hypercube': 19.6176,
    'IVFFlat': 1.5543,
    'IVFPQ': 12.2624,
    'NLSH': 71.2496
}

recall_data = {
    'LSH': 20.00,
    'Hypercube': 5.00,
    'IVFFlat': 20.00,
    'IVFPQ': 15.00,
    'NLSH': 6.67
}

print("\n" + "="*90)
print(" "*20 + "SPEED vs ACCURACY TRADE-OFF ANALYSIS")
print("="*90)

print(f"\n{'Method':<15} {'Recall@5 %':<15} {'QPS (queries/sec)':<20} {'Efficiency Score*':<20}")
print("-"*90)

for method in ['LSH', 'IVFFlat', 'IVFPQ', 'NLSH', 'Hypercube']:
    recall = recall_data[method]
    qps = qps_data[method]
    
    # Efficiency score: (recall * qps) / 100
    # Balances accuracy with speed
    efficiency = (recall * qps) / 100
    
    # Visual representation
    efficiency_bar = "█" * int(efficiency) + "░" * max(0, 15 - int(efficiency))
    
    print(f"{method:<15} {recall:>6.2f}%         {qps:>12.2f}            {efficiency:>6.2f}  {efficiency_bar}")

print("-"*90)
print("* Efficiency Score = (Recall × QPS) / 100")
print("  Captures both accuracy and speed in single metric")

print("\n" + "="*90)
print("INTERPRETATION")
print("="*90)

print("""
Method Characteristics:

1. LSH (Locality Sensitive Hashing)
   • Recall: 20% (BEST)
   • QPS: 0.70 (SLOWEST)
   • Trade-off: Prioritizes accuracy but very slow
   • Use case: Offline analysis, when accuracy is critical

2. IVFFlat (Inverted File with Flat Quantization)
   • Recall: 20% (BEST)
   • QPS: 1.55 (SLOW)
   • Trade-off: Best recall with reasonable speed
   • Use case: RECOMMENDED for production systems
   
3. IVFPQ (Inverted File with Product Quantization)
   • Recall: 15% (GOOD)
   • QPS: 12.26 (FAST)
   • Trade-off: Good balance of recall and speed
   • Use case: When speed is somewhat important
   
4. NLSH (Neural LSH)
   • Recall: 6.67% (FAIR)
   • QPS: 71.25 (FASTEST)
   • Trade-off: Prioritizes speed over accuracy
   • Use case: Quick screening of very large databases
   
5. Hypercube
   • Recall: 5% (POOREST)
   • QPS: 19.62 (FAST)
   • Trade-off: Some speed but poor recall
   • Use case: Not recommended

WINNER BY CATEGORY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥇 BEST OVERALL (Accuracy): IVFFlat (20% recall, 1.55 QPS)
🥈 BEST BALANCED: IVFFlat (Highest efficiency score)
🥉 FASTEST: NLSH (71.25 QPS, but only 6.67% recall)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATIONS:
• For high-accuracy needs → Use IVFFlat or LSH
• For balanced system → Use IVFFlat  
• For extremely large database → Use NLSH or IVFPQ
• Combine with BLAST for validation of candidates
""")

print("="*90)
