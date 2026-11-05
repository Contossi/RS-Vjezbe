const currency = new Intl.NumberFormat('hr-HR', { style: 'currency', currency: 'EUR' })

export const formatPrice = (value) => currency.format(value)
