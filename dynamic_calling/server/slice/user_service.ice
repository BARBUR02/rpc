module UserService 
{
    struct UserData 
    {
        string name;
        int age;
    };

    sequence<UserData> Users;

    interface DynamicUserService 
    {
        void sayHello();
        
        void addUser(UserData userData);
        
        Users getUsers();
        
        void processUserList(Users userList);
    }
}
