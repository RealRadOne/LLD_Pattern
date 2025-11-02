import java.util.*;
abstract class Item 
{
    int ID;
    String name;
    int price;
    Item(String name)
    {
        this.ID+=1;
        this.name = name;
    }
    abstract int getPrice();
}
class ItemA extends Item
{
    ItemA()
    {
        super("ItemA");
    }

    @Override 
    int getPrice()
    {
        return 10;
    }
}
class ItemB extends Item
{
    ItemB()
    {
        super("ItemB");
    }

    @Override 
    int getPrice()
    {
        return 20;
    }
}
class ItemFactory
{
    public static Item createItem(String name)
    {
        switch(name)
        {
            case "ItemA":
                return new ItemA();
            case "ItemB":
                return new ItemB();
            default:
                throw new IllegalArgumentException("Unknown type");
        }
    }
}
class Money
{
    int value;
    int getValue()
    {
        return this.value;
    }
}
class Inventory 
{
    HashMap<String,Integer>stock     = new HashMap<String,Integer>();
    HashMap<Integer,Integer>currency = new HashMap<Integer,Integer>();

    void show_inventory()
    {
        for(String items:stock.keySet())
        {
            System.out.println("Showing the item name it's price and inventory");
            System.out.println(items+" "+stock.get(items));
        }
    }

    void add_Item(String item,int quantity)
    {
        if(stock.containsKey(item))
        {
            stock.put(item,stock.get(item)+quantity);
        }
        else 
            stock.put(item,quantity);
    }

    String get_Item(String name,int quantity,int amount)
    {
        Item item = ItemFactory.createItem(name);
        if(item.getPrice()*quantity>amount)
            return "Insufficient funds";
        else if(!stock.containsKey(name))
            return "Item Not Found";
        else 
        {
            stock.put(name,stock.get(name)-quantity);
            return "Providing item with name:"+name;
        }
    }

    void add_Money(int money,int quantity)
    {
        if(currency.containsKey(money))
        {
            currency.put(money,currency.get(money)+quantity);
        }
        else 
            currency.put(money,quantity);
    }

    String get_Money(int money)
    {
        if(!currency.containsKey(money))
            return "Insufficient change";
        else 
        {
            currency.put(money,currency.get(money)-1);
            return "Providing change of value:"+money;
        }
    }
}

class VendingMachine
{
    Inventory inv = new Inventory();
    void showMenu()
    {
        inv.show_inventory();
    }
    String buy(String name, int amount)
    {
       return inv.get_Item(name, amount, amount);
    }
}