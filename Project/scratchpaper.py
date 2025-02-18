# WEEKLY_HOUR: int = 40



# # HOURLY_RATE_D: int = 29
# # HOURLY_RATE_C: float = 44.2308

# # Taxes that takes out of gross income
# SOCIAL_SECURITY: float = 0.062
# MEDICARE: float = 0.0145
# CA_SDI: float = 0.0115

# def annual_gross_income(hourly_rate: float) -> float:
#     return hourly_rate * WEEKLY_HOUR * 52

# def annual_gross_household_income() -> float:
#     hourly_rate1 = 29
#     hourly_rate2 = 44.2308
#     return (hourly_rate1 + hourly_rate2) * WEEKLY_HOUR * 52

# def annual_fixed_tax() -> float:
#     household_income = annual_gross_household_income(29, 44.2308)
#     fixed_tax = household_income * (SOCIAL_SECURITY + MEDICARE + CA_SDI)

#     return fixed_tax

# def fixed_pre_tax_deduction(amount: float) -> float:
#     return amount * 52

# def fixed_post_tax_deduction(amount: float) -> float:
#     return 0

# def traditional_401k_deduction(percentage: float) -> float:

#     return 0

# def 

# # print(annual_gross_household_income(29, 44.2308))
# # print(annual_fixed_tax())


"""
2025 401(k) and Tax Calculator for Married Couples (Filing Jointly)
- Uses 2025 IRS tax brackets and CA state tax rates.
- Separates federal, state, and payroll tax calculations.
- Implements progressive tax brackets instead of flat rates.
"""

# --------------------------
# 2025 Tax Constants (IRS and CA)
# --------------------------
STANDARD_DEDUCTION = 30000  # Married filing jointly

# Federal Tax Brackets (Married Filing Jointly)
FEDERAL_BRACKETS = [
    (23850, 0.10),    # 10% up to $23,850
    (73100, 0.12),    # 12% up to $73,100 (23,850 + 49,250)
    (float('inf'), 0.22)  # 22% above $96,950 (73,100 + 23,850)
]

# CA State Tax Brackets (Married Filing Jointly)
CA_BRACKETS = [
    (22804, 0.01),    # 1% up to $22,804
    (54022, 0.02),    # 2% up to $54,022
    (68084, 0.04),    # 4% up to $68,084
    (108162, 0.06),   # 6% up to $108,162
    (136700, 0.08),   # 8% up to $136,700
    (float('inf'), 0.093)  # 9.3% above $136,700
]

# Payroll Taxes
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
CA_SDI_RATE = 0.011  # 1.1% of taxable wages up to $153,164 (2025 limit)

# --------------------------
# Tax Calculation Functions
# --------------------------
def calculate_income_tax(income, brackets):
    """Calculate tax using progressive brackets."""
    tax = 0
    prev_limit = 0
    for limit, rate in brackets:
        if income <= 0:
            break
        bracket_amount = min(income, limit - prev_limit)
        tax += bracket_amount * rate
        income -= bracket_amount
        prev_limit = limit
    return tax

def calculate_federal_withholding(taxable_income):
    """Federal income tax withholding using 2025 brackets."""
    return calculate_income_tax(taxable_income, FEDERAL_BRACKETS)

def calculate_ca_state_tax(taxable_income):
    """CA state income tax using 2025 brackets."""
    return calculate_income_tax(taxable_income, CA_BRACKETS)

def calculate_payroll_taxes(gross_pay):
    """Calculate FICA taxes and CA SDI."""
    social_security = gross_pay * SOCIAL_SECURITY_RATE
    medicare = gross_pay * MEDICARE_RATE
    ca_sdi = min(gross_pay, 153164/26) * CA_SDI_RATE  # Biweekly SDI cap
    return social_security, medicare, ca_sdi

# --------------------------
# Paycheck Calculator
# --------------------------
def calculate_paycheck(gross_pay, contribution_rate, pay_periods, other_pre_tax=0):
    """
    Calculate net pay with 2025 tax rules.
    
    Args:
        gross_pay: Gross pay per paycheck
        contribution_rate: 401(k) contribution rate (0-1)
        pay_periods: Number of pay periods per year (26 for biweekly, 52 for weekly)
        other_pre_tax: Other pre-tax deductions (health insurance, etc.)
        
    Returns:
        Dictionary with paycheck details
    """
    # Pre-tax deductions
    k401_contribution = gross_pay * contribution_rate
    taxable_wage = gross_pay - k401_contribution - other_pre_tax
    
    # Tax calculations
    federal_tax = calculate_federal_withholding(taxable_wage * pay_periods) / pay_periods
    state_tax = calculate_ca_state_tax(taxable_wage * pay_periods) / pay_periods
    social_security, medicare, ca_sdi = calculate_payroll_taxes(gross_pay)
    
    # Total deductions
    total_deductions = (k401_contribution + federal_tax + state_tax +
                       social_security + medicare + ca_sdi)
    
    return {
        'gross_pay': gross_pay,
        '401k_contribution': k401_contribution,
        'taxable_wage': taxable_wage,
        'federal_tax': federal_tax,
        'state_tax': state_tax,
        'social_security': social_security,
        'medicare': medicare,
        'ca_sdi': ca_sdi,
        'total_deductions': total_deductions,
        'net_pay': gross_pay - total_deductions
    }

# --------------------------
# Main Execution
# --------------------------
def main():
    # Your paycheck (weekly)
    your_paycheck = calculate_paycheck(
        gross_pay=1160,
        contribution_rate=0.06,
        pay_periods=52,
        other_pre_tax=0
    )
    
    # Husband's paycheck (biweekly)
    husband_paycheck = calculate_paycheck(
        gross_pay=3538.46,
        contribution_rate=0.01,
        pay_periods=26,
        other_pre_tax=129.10  # Dental/medical/vision
    )
    
    # Annual tax calculation
    combined_taxable = (
        your_paycheck['taxable_wage'] * 52 +
        husband_paycheck['taxable_wage'] * 26
    )
    adjusted_taxable = combined_taxable - STANDARD_DEDUCTION
    annual_federal_tax = calculate_federal_withholding(adjusted_taxable)
    
    # Print results
    print("=== Your Weekly Paycheck ===")
    for key, val in your_paycheck.items():
        print(f"{key:>18}: ${val:.2f}")
    
    print("\n=== Husband's Biweekly Paycheck ===")
    for key, val in husband_paycheck.items():
        print(f"{key:>18}: ${val:.2f}")
    
    print("\n=== Annual Household Taxes ===")
    print(f"{'Combined Taxable Income':>30}: ${combined_taxable:,.2f}")
    print(f"{'After Standard Deduction':>30}: ${adjusted_taxable:,.2f}")
    print(f"{'Federal Tax Liability':>30}: ${annual_federal_tax:,.2f}")

if __name__ == "__main__":
    main()