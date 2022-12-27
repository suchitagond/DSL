#include <iostream>
using namespace std;

struct link *creat(int count, struct link *head);

void display(struct link *head);

void A_U_B();
void A_int_B();
void A_min_B();
void B_min_A();
void U_min_A_U_B();

struct link
{
    char data;
    struct link *next;
} * head_union, *head_A, *head_B ;

int main()
{
    head_union = head_A = head_B = NULL;

    for (int i = 1; i < 4; i++)
    {
        if (i == 1)
        {
            int a;
            cout << "no. of student like vanilla icecream :";
            cin >> a;
            head_A = creat(a, head_A);
            cout << "\n";
            display(head_A);
        }
        if (i == 2)
        {
            int b;
            cout << "no. of student like butterscotch icecream :";
            cin >> b;
            head_B = creat(b, head_B);
            cout << "\n";
            display(head_B);
        }
        if (i == 3)
        {
            int c;
            cout << "no. of student in class :";
            cin >> c;
            head_union = creat(c, head_union);
            cout << "\n";
            display(head_union);
        }
    }
    cout << "set A :";
    display(head_A);
    cout << "set B :";
    display(head_B);
    cout << "set union :";
    display(head_union);
    cout << "\n";

    A_U_B();
    A_int_B();
    A_min_B();
    B_min_A();
    U_min_A_U_B();

    return 0;
}
struct link *creat(int count, struct link *head)
{
    struct link *s, *newNode;

    for (int i = 0; i < count; i++)
    {
        newNode = new (struct link);
        cout << "enter roll no of student :";
        cin >> newNode->data;
        newNode->next = NULL;

        if (head == NULL)
        {
            head = newNode;
            s = head;
        }
        else
        {
            s->next = newNode;
            s = s->next;
        }
    }
    return head;
}

void display(struct link *head)
{
    struct link *m;
    m = head;
    while (m != NULL)
    {
        cout << " " << m->data;
        m = m->next;
    }
}
void A_U_B()
{
    struct link *p, *q;
    p = head_A;
    q = head_B;
    char a[20];
    int i = 0;
    while (p != NULL && q != NULL)
    {
        if (p->data == q->data)
        {
            a[i] = p->data;
            i++;
            p = p->next;
            q = q->next;
        }
        else
        {
            a[i] = p->data;
            i++;
            p = p->next;
        }
    }
    if (p == NULL)
    {
        while (q != NULL)
        {
            a[i] = q->data;
            i++;
            q = q->next;
        }
    }
    if (q == NULL)
    {
        while (p != NULL)
        {
            a[i] = p->data;
            i++;
            p = p->next;
        }
    }
    cout << "set A union B : ";
    for (int j = 0; j < i; j++)
    {
        cout << " " << a[j];
    }
}

void A_int_B()
{
    struct link *p, *q;
    char b[20];
    p = head_A;
    q = head_B;
    int i = 0;
    while (p != NULL)
    {
        while (q != NULL)
        {
            if (p->data == q->data)
            {
                b[i] = p->data;
                i++;
                break;
            }
            q = q->next;
        }
        p = p->next;
    }

    cout << "set A intersection B : ";
    for (int j = 0; j < i; j++)
    {
        cout << " " << b[j];
    }
}

void A_min_B()
{
    struct link *p, *q;
    int i = 0;
    char c[20];
    p = head_A;
    q = head_B;
    while (p != NULL)
    {
        int flag = 0;
        while (q != NULL)
        {
            if (p->data == q->data)
            {
                flag = 1;
                break;
            }
            q = q->next;
        }
        if (flag == 0)
        {
            c[i] = p->data;
            i++;
        }
        p = p->next;
    }

    cout << "set A minues B : ";
    for (int j = 0; j < i; j++)
    {
        cout << " " << c[j];
    }
}

void B_min_A()
{
    struct link *p, *q;
    int i = 0;
    char d[20];
    p = head_A;
    q = head_B;
    while (q != NULL)
    {
        int flag = 0;
        while (p != NULL)
        {
            if (p->data == q->data)
            {
                flag = 1;
                break;
            }
            p = p->next;
        }
        if (flag == 0)
        {
            d[i] = q->data;
            i++;
        }
        q = q->next;
    }

    cout << "set B minus A : ";
    for (int j = 0; j < i; j++)
    {
        cout << " " << d[j];
    }
}

void U_min_A_U_B()
{
    struct link *p, *q, *r;
    char e[20];
    int i = 0;
    p = head_A;
    q = head_B;
    r = head_union;
    while (r != NULL)
    {
        int flag = 0;
        while (p != NULL)
        {
            if (r->data == p->data)
            {
                flag = 1;
                break;
            }
            p = p->next;
        }
        while (q != NULL)
        {
            if (r->data == q->data)
            {
                flag = 1;
                break;
            }
            q = q->next;
        }
        if (flag == 0)
        {
            e[i] = r->data;
            i++;
        }
    }

    cout << "set U minus A union B : ";
    for (int j = 0; j < i; j++)
    {
        cout << " " << e[j];
    }
}