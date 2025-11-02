import java.util.HashMap;

abstract class Car
{
    String model;
    int price;
    Car(String model)
    {
        this.model = model;
    }
    abstract void set_price();
    abstract int get_price();
}

class Sedan extends Car 
{
    Sedan()
    {
        super("sedan");
    }

    @Override
    void set_price()
    {
        this.price = 100;
    }

    @Override
    int get_price()
    {
        return this.price;
    }
}

class SUV extends Car 
{
    SUV()
    {
        super("SUV");
    }

    @Override
    void set_price()
    {
        this.price = 100;
    }

    @Override
    int get_price()
    {
        return this.price;
    }
}

class CarFactory
{
    public static Car createCar(String type)
    {
        switch(type)
        {
            case "Sedan":
                return new Sedan();
            case "SUV":
                return new SUV();
            default:
                throw new IllegalArgumentException("Unknown type");
        }
    }
}

class Payment
{
    int get_Price(String car_type)
    {
        Car car = CarFactory.createCar(car_type);
        return car.get_price();
    }
    
    int makePayment(String car_type,int amount)
    {
        int car_price = get_Price(car_type);
        if(car_price>amount)
            return -1;
        else 
            return amount-car_price;
    }
}

class Inventory 
{
    HashMap<String,Integer>stock = new HashMap<String,Integer>();

    void add_stock(String type,int number)
    {
        int inventory = number;
        if(stock.containsKey(type))
            inventory+=stock.get(type);
        stock.put(type,inventory);
    }

    int get_car(String type,int number)
    {
        if(!stock.containsKey(type))
            return -1;
        else if(stock.get(type)<number) 
            return -1;
        else 
        {
            stock.put(type,stock.get(type)-number);
            return 200;
        } 
    }

}

class CarInterface
{
    Inventory it = new Inventory();
    Payment ps = new Payment();

    void buyCar(String type,int amount,int number)
    {
        int status = it.get_car(type, number);
        if(status ==200)
            ps.makePayment(type, amount);
        else 
            System.out.println("Car unavaiable or amount insufficient");
    }
}