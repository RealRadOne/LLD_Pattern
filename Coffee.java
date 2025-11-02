//Trying to implement factory pattern
public abstract class Coffee
{
    private int price;
    public Coffee(int price)
    {
        this.price = price;
    }
    int getPrice()
    {
        return this.price;
    };
    abstract void brew();
    abstract int getSugar();
    abstract int getMilk();
    abstract int getCoffee();
}

class Espresso extends Coffee
{
    Espresso()
    {
        super(10);
    }

    @Override
    void brew()
    {
        System.out.println("Brewing espresso");
    }
    @Override
    int getSugar(){return 1;}
    @Override
    int getMilk(){return 0;}
    @Override
    int getCoffee(){return 10;}
}

class Latte extends Coffee
{
    Latte()
    {
        super(20);
    }
    
    @Override
    void brew()
    {
        System.out.println("Brewing Latte");
    }
    @Override
    int getSugar(){return 2;}
    @Override
    int getMilk(){return 3;}
    @Override
    int getCoffee(){return 6;}
}

class CoffeeFactory
{
    public static Coffee createCoffee(String type)
    {
        switch(type)
        {
            case "Espresso":
                return new Espresso();
            case "Latte":
                return new Latte();
            default:
                throw new IllegalArgumentException("Unknown type");
        }
    }
}
//Creating an inventory class for managing vending machine
class Inventory
{
    private int sugar;
    private int milk;
    private int coffee;

    private Inventory()
    {
        this.sugar = 10;
        this.milk = 10;
        this.coffee = 10;
    }

    void add_sugar(int sugar)
    {
        this.sugar+=sugar;
    }
    void get_sugar(int sugar)
    {
        if(this.sugar==0)
            System.out.println("No sugar left");
        else 
            this.sugar-=sugar;
    }
    void add_milk(int milk)
    {
        this.milk+=milk;
    }
    void get_milk(int milk)
    {
        if(this.milk==0)
            System.out.println("No sugar left");
        else 
            this.milk-=milk;
    }
    void add_coffee(int coffee)
    {
        this.coffee+=coffee;
    }
    void get_coffee(int coffee)
    {
        if(this.coffee==0)
            System.out.println("No sugar left");
        else 
            this.coffee-=coffee;
    }
}
class VendingMachine
{
    void take_order(String type,int money)
    {
        Coffee coffee = CoffeeFactory.createCoffee(type);
        if(coffee.getPrice()>money)
            System.out.println("Charges insufficient");
        else 
            coffee.brew();
    }
}