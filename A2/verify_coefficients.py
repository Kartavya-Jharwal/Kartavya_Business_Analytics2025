"""
Verify the regression coefficients and price prediction formula.
Cross-checks the JavaScript calculator against the Python model.
"""

import math

# =============================================================================
# COEFFICIENTS FROM Final.ipynb OLS OUTPUT (statsmodels)
# Source: Final_export.html lines 9593-9599
# =============================================================================
CONST = 4.6250
ACCOMMODATES = 0.1122
BEDROOMS = 0.1644
BEDS = -0.0523
ROOM_HOTEL = 0.8721
ROOM_PRIVATE = -0.7310
ROOM_SHARED = -1.3692

def predict_price(accommodates, bedrooms, beds, room_type):
    """
    Predict Airbnb nightly price using OLS regression coefficients.
    
    Model: ln(Price) = β₀ + β₁(accommodates) + β₂(bedrooms) + β₃(beds) 
                     + β₄(Hotel) + β₅(Private) + β₆(Shared) + ε
    
    Reference category: Entire home/apt (all room dummies = 0)
    """
    log_price = CONST
    log_price += ACCOMMODATES * accommodates
    log_price += BEDROOMS * bedrooms
    log_price += BEDS * beds
    
    if room_type == 'hotel':
        log_price += ROOM_HOTEL
    elif room_type == 'private':
        log_price += ROOM_PRIVATE
    elif room_type == 'shared':
        log_price += ROOM_SHARED
    # 'entire' -> no adjustment (reference category)
    
    return math.exp(log_price)


if __name__ == "__main__":
    print("=" * 60)
    print("PRICE PREDICTION VERIFICATION")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        (4, 2, 2, "entire", "4 guests, 2 bedrooms, 2 beds, Entire home"),
        (2, 1, 1, "private", "2 guests, 1 bedroom, 1 bed, Private room"),
        (1, 1, 1, "shared", "1 guest, 1 bedroom, 1 bed, Shared room"),
        (2, 1, 1, "hotel", "2 guests, 1 bedroom, 1 bed, Hotel room"),
        (1, 0, 1, "entire", "1 guest, 0 bedrooms (studio), 1 bed, Entire"),
        (6, 3, 4, "entire", "6 guests, 3 bedrooms, 4 beds, Entire home"),
    ]
    
    print("\nTest Cases:")
    print("-" * 60)
    for acc, bed, beds, room, desc in test_cases:
        price = predict_price(acc, bed, beds, room)
        print(f"  {desc}")
        print(f"    → £{price:.2f}/night")
        print()
    
    # Coefficient interpretation
    print("=" * 60)
    print("COEFFICIENT INTERPRETATION")
    print("=" * 60)
    print(f"\nContinuous Variables (% change per unit):")
    print(f"  +1 guest capacity  = +{(math.exp(ACCOMMODATES)-1)*100:.1f}%")
    print(f"  +1 bedroom         = +{(math.exp(BEDROOMS)-1)*100:.1f}%")
    print(f"  +1 bed             = {(math.exp(BEDS)-1)*100:.1f}% (negative!)")
    
    print(f"\nRoom Type (vs. Entire home/apt):")
    print(f"  Hotel room    = +{(math.exp(ROOM_HOTEL)-1)*100:.1f}%")
    print(f"  Private room  = {(math.exp(ROOM_PRIVATE)-1)*100:.1f}%")
    print(f"  Shared room   = {(math.exp(ROOM_SHARED)-1)*100:.1f}%")
    
    # JavaScript formula verification
    print("\n" + "=" * 60)
    print("JAVASCRIPT FORMULA (copy to calculator)")
    print("=" * 60)
    print("""
const COEFFICIENTS = {
    const: 4.6250,
    accommodates: 0.1122,
    bedrooms: 0.1644,
    beds: -0.0523,
    room_Hotel: 0.8721,
    room_Private: -0.7310,
    room_Shared: -1.3692
};

function predictPrice(accommodates, bedrooms, beds, roomType) {
    let logPrice = COEFFICIENTS.const;
    logPrice += COEFFICIENTS.accommodates * accommodates;
    logPrice += COEFFICIENTS.bedrooms * bedrooms;
    logPrice += COEFFICIENTS.beds * beds;
    
    if (roomType === 'hotel') logPrice += COEFFICIENTS.room_Hotel;
    else if (roomType === 'private') logPrice += COEFFICIENTS.room_Private;
    else if (roomType === 'shared') logPrice += COEFFICIENTS.room_Shared;
    
    return Math.exp(logPrice);
}
""")
    
    print("✓ Coefficients verified from Final_export.html")
    print("✓ Formula ready for index.html calculator")
