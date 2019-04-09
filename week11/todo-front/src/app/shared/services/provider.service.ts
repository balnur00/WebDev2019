import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import { TaskList, Task } from '../models/model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTasksList(): Promise<TaskList[]>{
    return this.get('http://localhost:8000/api/tasklist/', {})
  }
  getTasks(id: number): Promise<Task[]>{
  	return this.get(`http://localhost:8000/api/tasklist/${id}/task`, {})
  }
}
