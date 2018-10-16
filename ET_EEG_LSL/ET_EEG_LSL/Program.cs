using System;
using System.Collections.Generic;
using System.Threading;
using LSL;
using Tobii.Interaction;


namespace ET_EEG_LSL
{
    class Program
    {
        private static Host _host;
        private static GazePointDataStream _gazePointDataStream;
        private static List<double> s1 = new List<double>();
        public static double [] sample = new double[3];
        public static double eye_x = 0;
        public static double eye_y = 0;
        public static double time_st = 0;


        private static void InitializeHost()
        {
            _host = new Host();
        }
        private static void DisableConnectionWithTobiiEngine()
        {
            _host.DisableConnection();
        }

        private static void CreateAndVisualizeLightlyFilteredGazePointStream()
        {
            _gazePointDataStream = _host.Streams.CreateGazePointDataStream();
            _gazePointDataStream.GazePoint((x, y, ts) => {
                s1.Add(ts);
                time_st = ts - s1[0];
                eye_x = x;
                eye_y = y;

            });

        }

        static void Main(string[] args)
        {

            // create stream info and outlet
            liblsl.StreamInfo info = new liblsl.StreamInfo("Tobii", "Gaze", 3, 60, liblsl.channel_format_t.cf_float32, "eye_tracker");
            liblsl.StreamOutlet outlet = new liblsl.StreamOutlet(info);
            InitializeHost();
            ConsoleKeyInfo keyinfo;
            //Console.WriteLine(sample.ToString());

            do
            {
                keyinfo = Console.ReadKey();

                while (!Console.KeyAvailable)
                {
                    CreateAndVisualizeLightlyFilteredGazePointStream();
                    Console.WriteLine(time_st.ToString() + "  " + eye_x.ToString() + "  " + eye_y.ToString());
                    sample[0] = time_st;
                    sample[1] = eye_x;
                    sample[2] = eye_y;
                
                    outlet.push_sample(sample);
                    System.Threading.Thread.Sleep(10);
                }

            }
            while (keyinfo.Key != ConsoleKey.Spacebar);
            DisableConnectionWithTobiiEngine();
        }
    }
}