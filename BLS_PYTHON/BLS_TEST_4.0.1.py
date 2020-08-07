#>>> from bls_datasets import oes, qcew

# OES example:

>> > df_oes = oes.get_data(year=2017)
>> > df_oes.columns
Index(['OCC_CODE', 'OCC_TITLE', 'OCC_GROUP', 'TOT_EMP', 'EMP_PRSE', 'H_MEAN',
       'A_MEAN', 'MEAN_PRSE', 'H_PCT10', 'H_PCT25', 'H_MEDIAN', 'H_PCT75',
       'H_PCT90', 'A_PCT10', 'A_PCT25', 'A_MEDIAN', 'A_PCT75', 'A_PCT90',
       'ANNUAL', 'HOURLY'],
      dtype='object')

# Which occupation had the highest total employment in 2017?

>> > detailed = df_oes[df_oes.OCC_GROUP == 'detailed']
>> > detailed[detailed.TOT_EMP == detailed.TOT_EMP.max()].OCC_TITLE
772    Retail Salespersons

# QCEW example:
>> > df_qcew = qcew.get_data('industry', rtype='dataframe', year='2017',
                             ...             qtr='1', industry='10')
>> > df_qcew.columns
Index(['area_fips', 'own_code', 'industry_code', 'agglvl_code', 'size_code',
       'year', 'qtr', 'disclosure_code', 'qtrly_estabs', 'month1_emplvl',
       'month2_emplvl', 'month3_emplvl', 'total_qtrly_wages',
       'taxable_qtrly_wages', 'qtrly_contributions', 'avg_wkly_wage',
       'lq_disclosure_code', 'lq_qtrly_estabs', 'lq_month1_emplvl',
       'lq_month2_emplvl', 'lq_month3_emplvl', 'lq_total_qtrly_wages',
       'lq_taxable_qtrly_wages', 'lq_qtrly_contributions', 'lq_avg_wkly_wage',
       'oty_disclosure_code', 'oty_qtrly_estabs_chg',
       'oty_qtrly_estabs_pct_chg', 'oty_month1_emplvl_chg',
       'oty_month1_emplvl_pct_chg', 'oty_month2_emplvl_chg',
       'oty_month2_emplvl_pct_chg', 'oty_month3_emplvl_chg',
       'oty_month3_emplvl_pct_chg', 'oty_total_qtrly_wages_chg',
       'oty_total_qtrly_wages_pct_chg', 'oty_taxable_qtrly_wages_chg',
       'oty_taxable_qtrly_wages_pct_chg', 'oty_qtrly_contributions_chg',
       'oty_qtrly_contributions_pct_chg', 'oty_avg_wkly_wage_chg',
       'oty_avg_wkly_wage_pct_chg'],
      dtype='object')

# What were the average weekly earnings in Fresno County for 2017 Q1?

# FIPS code, area title
# 06019, Fresno County, California

>> > fresno = df_qcew[(df_qcew.own_code == 0) & (df_qcew.area_fips == '06019')]
>> > fresno.avg_wkly_wage.values[0]
803
