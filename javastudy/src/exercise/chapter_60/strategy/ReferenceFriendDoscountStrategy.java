package exercise.chapter_60.strategy;

public class ReferenceFriendDoscountStrategy implements DiscountStrategy {
    @Override
    public double calculateDiscount(double amount) {
        return amount * 0.15;
    }
}
