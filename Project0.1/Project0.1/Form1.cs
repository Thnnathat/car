using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Project0._1
{
    public partial class Form1 : Form
    {
        NetworkHelper con = new NetworkHelper("192.168.192.149:8000");
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string path = "/car/values_gyro";
            string param = "";
            var data = con.getData(path, param);
            if (data != null)
            {
                label6.Text = data[0]["ay"];
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
           
        }

        private void label6_Click(object sender, EventArgs e)
        {

        }

    }
}
